# -*- coding: utf-8 -*-
# ==============================================================================
# MIT License
#
# Copyright (c) 2021 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

import weakref
from abc import ABC
from typing import Optional

from dimsdk import ID

from startrek.fsm import Context, BaseTransition, BaseState, AutoMachine
from startrek import DockerStatus

from .session import ClientSession


class StateMachine(AutoMachine, Context):

    def __init__(self, session: ClientSession):
        super().__init__(default=SessionState.DEFAULT)
        self.__session = weakref.ref(session)
        # init states
        builder = self._create_state_builder()
        self.__set_state(state=builder.get_default_state())
        self.__set_state(state=builder.get_connecting_state())
        self.__set_state(state=builder.get_connected_state())
        self.__set_state(state=builder.get_handshaking_state())
        self.__set_state(state=builder.get_running_state())
        self.__set_state(state=builder.get_error_state())

    @property
    def session(self) -> ClientSession:
        return self.__session()

    # noinspection PyMethodMayBeStatic
    def _create_state_builder(self):
        from .transition import TransitionBuilder
        return StateBuilder(transition_builder=TransitionBuilder())

    def __set_state(self, state):
        self.set_state(name=state.name, state=state)

    @property  # Override
    def context(self) -> Context:
        return self

    @property
    def session_key(self) -> Optional[str]:
        session = self.session
        return session.key

    @property
    def session_id(self) -> ID:
        session = self.session
        return session.identifier

    @property
    def status(self) -> DockerStatus:
        session = self.session
        gate = session.gate
        docker = gate.fetch_docker(remote=session.remote_address, local=None, advance_party=[])
        if docker is None:
            return DockerStatus.ERROR
        else:
            return docker.status


# noinspection PyAbstractClass
class StateTransition(BaseTransition[StateMachine], ABC):

    # noinspection PyMethodMayBeStatic
    def is_expired(self, state, now: float) -> bool:
        assert isinstance(state, SessionState), 'state error: %s' % state
        return 0 < state.enter_time < (now - 30)


class SessionState(BaseState[StateMachine, StateTransition]):
    """
        Session State
        ~~~~~~~~~~~~~

        Defined for indicating session states

            DEFAULT     - initialized
            CONNECTING  - connecting to station
            CONNECTED   - connected to station
            HANDSHAKING - trying to log in
            RUNNING     - handshake accepted
            ERROR       - network error
    """

    DEFAULT = 'default'
    CONNECTING = 'connecting'
    CONNECTED = 'connected'
    HANDSHAKING = 'handshaking'
    RUNNING = 'running'
    ERROR = 'error'

    def __init__(self, name: str):
        super().__init__()
        self.__name = name
        self.__time: float = 0  # enter time

    @property
    def name(self) -> str:
        return self.__name

    @property
    def enter_time(self) -> float:
        return self.__time

    def __str__(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return self.__name

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        elif isinstance(other, SessionState):
            return self.__name == other.name
        elif isinstance(other, str):
            return self.__name == other
        else:
            return False

    def __ne__(self, other) -> bool:
        if self is other:
            return False
        elif isinstance(other, SessionState):
            return self.__name != other.name
        elif isinstance(other, str):
            return self.__name != other
        else:
            return True

    # Override
    def on_enter(self, old, ctx: StateMachine, now: float):
        self.__time = now

    # Override
    def on_exit(self, new, ctx: StateMachine, now: float):
        self.__time = 0

    # Override
    def on_pause(self, ctx: StateMachine):
        pass

    # Override
    def on_resume(self, ctx: StateMachine):
        pass


#
#   Builders
#

class StateBuilder:

    def __init__(self, transition_builder):
        super().__init__()
        self.__builder = transition_builder

    # noinspection PyMethodMayBeStatic
    def get_named_state(self, name: str) -> SessionState:
        return SessionState(name=name)

    def get_default_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.DEFAULT)
        # Default -> Connecting
        state.add_transition(transition=builder.get_default_connecting_transition())
        return state

    def get_connecting_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.CONNECTING)
        # Connecting -> Connected
        state.add_transition(transition=builder.get_connecting_connected_transition())
        # Connecting -> Error
        state.add_transition(transition=builder.get_connecting_error_transition())
        return state

    def get_connected_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.CONNECTED)
        # Connected -> Handshaking
        state.add_transition(transition=builder.get_connected_handshaking_transition())
        # Connected -> Error
        state.add_transition(transition=builder.get_connected_error_transition())
        return state

    def get_handshaking_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.HANDSHAKING)
        # Handshaking -> Running
        state.add_transition(transition=builder.get_handshaking_running_transition())
        # Handshaking -> Connected
        state.add_transition(transition=builder.get_handshaking_connected_transition())
        # Handshaking -> Error
        state.add_transition(transition=builder.get_handshaking_error_transition())
        return state

    def get_running_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.RUNNING)
        # Running -> Default
        state.add_transition(transition=builder.get_running_default_transition())
        # Running -> Error
        state.add_transition(transition=builder.get_running_error_transition())
        return state

    def get_error_state(self) -> SessionState:
        builder = self.__builder
        # assert isinstance(builder, TransitionBuilder)
        state = self.get_named_state(name=SessionState.ERROR)
        # Error -> Default
        state.add_transition(transition=builder.get_error_default_transition())
        return state

from __future__ import annotations
from typing import Literal
from collections import UserDict


class State(UserDict):
    pass


class Step:
    def action(self, state: State):
        pass

    def compensate(self, state: State):
        pass


class Saga:
    state: State
    steps: list[Step]
    status: Literal["success", "rollback", "error"]
    _execute_exc: Exception
    _rollback_exc: Exception
    _current_index: int
    _error_index: int

    def __init__(self, steps: list[Step] = None, state: State = None):
        """Configure saga steps and init state if needed"""
        self.steps = steps or []
        self.state = state or State()

    def run(self):
        try:
            self._execute()
        except Exception as exc1:
            self._execute_exc = exc1
            try:
                self._rollback()
                self.status = "rollback"
            except Exception as exc2:
                self._rollback_exc = exc2
                self._error_index = self._current_index
                self.status = "error"
                raise exc2
            return self._failure()
        else:
            self.status = "success"
            return self._success()

    def _execute(self):
        self._current_index = 0
        for idx, step in enumerate(self.steps):
            self._current_index = idx
            step.action(self.state)

    def _rollback(self):
        for idx in range(self._current_index - 1, -1, -1):
            self._current_index = idx
            self.steps[idx].compensate(self.state)

    def _success(self):
        pass

    def _failure(self):
        pass

    def _error(self):
        pass

    @property
    def is_success(self):
        return self.status == "success"

    @property
    def is_rollback(self):
        return self.status == "rollback"

    @property
    def is_error(self):
        return self.status == "error"

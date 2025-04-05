"""
Refine related exceptions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import msgspec


class RefineError(Exception):
    """
    Refine specific exception.
    """


class InvalidConfigError(msgspec.ValidationError):
    """
    Validation error.
    """


class ConfigLoadError(RefineError):
    """
    Configuration loading error.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class RefineSystemExit(SystemExit):
    """
    Refine system exit exception that accepts a message argument.
    """

    code: int
    message: str | None

    def __init__(self, code: int, message: str | None = None):
        if TYPE_CHECKING:
            assert code is not None
            assert isinstance(code, int)
        super().__init__(code)
        self.message = message

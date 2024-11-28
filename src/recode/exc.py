"""
re:Code related exceptions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING


class ReCodeError(Exception):
    """
    re:Code specific exception.
    """


class ReCodeSystemExit(SystemExit):
    """
    re:Code system exit exception that accepts a message argument.
    """

    code: int
    message: str | None

    def __init__(self, code: int, message: str | None = None):
        if TYPE_CHECKING:
            assert code is not None
            assert isinstance(code, int)
        super().__init__(code)
        self.message = message

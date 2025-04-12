"""Utility functions."""
from typing import Literal

__all__ = ('on_off',)


def on_off(val: bool) -> Literal['on', 'off']:  # noqa: FBT001
    return 'on' if val else 'off'

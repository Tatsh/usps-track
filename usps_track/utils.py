"""Utility functions."""
from __future__ import annotations

from typing import Literal

__all__ = ('on_off',)


def on_off(val: bool) -> Literal['on', 'off']:  # noqa: FBT001
    """
    Convert a boolean value to ``'on'`` or ``'off'``.

    Parameters
    ----------
    val : bool
        The boolean value to convert.

    Returns
    -------
    Literal['on', 'off']
        ``'on'`` if *val* is truthy, ``'off'`` otherwise.
    """
    return 'on' if val else 'off'

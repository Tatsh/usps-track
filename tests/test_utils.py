from __future__ import annotations

from usps_track.utils import on_off


def test_utils_on_off() -> None:
    assert on_off(True) == 'on'  # noqa: FBT003
    assert on_off(False) == 'off'  # noqa: FBT003

from __future__ import annotations

from typing import TYPE_CHECKING
import logging

from usps_track.main import main

if TYPE_CHECKING:
    from click.testing import CliRunner
    from pytest_mock import MockerFixture


def test_main_number_with_leading_no_dashes(runner: CliRunner, mocker: MockerFixture) -> None:
    usps_track = mocker.patch('usps_track.main.usps_track')
    basic_config = mocker.patch('usps_track.main.logging.basicConfig')
    result = runner.invoke(main, ('123456', '15555555555'))
    assert result.exit_code == 0
    basic_config.assert_called_once_with(level=logging.ERROR)
    usps_track.assert_called_once_with('555-555-5555', ('123456',), [], raise_for_status=True)


def test_main_accept_number_with_no_leading(runner: CliRunner, mocker: MockerFixture) -> None:
    usps_track = mocker.patch('usps_track.main.usps_track')
    basic_config = mocker.patch('usps_track.main.logging.basicConfig')
    result = runner.invoke(main, ('123456', '555-555-5555'))
    assert result.exit_code == 0
    basic_config.assert_called_once_with(level=logging.ERROR)
    usps_track.assert_called_once_with('555-555-5555', ('123456',), [], raise_for_status=True)


def test_main_debug(runner: CliRunner, mocker: MockerFixture) -> None:
    usps_track = mocker.patch('usps_track.main.usps_track')
    basic_config = mocker.patch('usps_track.main.logging.basicConfig')
    tc = mocker.Mock()
    mocker.patch('usps_track.main.TraceConfig', return_value=tc)
    result = runner.invoke(main, ('123456', '5555555555', '--debug'))
    assert result.exit_code == 0
    basic_config.assert_called_once_with(level=logging.DEBUG)
    usps_track.assert_called_once_with('555-555-5555', ('123456',), [tc], raise_for_status=True)

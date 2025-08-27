from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import AsyncMock

from aiohttp import ContentTypeError
from usps_track.lib import TextServiceError, usps_track
import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


@pytest.mark.asyncio
async def test_usps_track_success(mocker: MockerFixture) -> None:
    mock_session_get = mocker.MagicMock()
    mock_session_get.return_value.__aenter__.return_value.text = AsyncMock(return_value='')
    mock_session_post = mocker.MagicMock()
    mock_session_post.return_value.__aenter__.return_value.json = AsyncMock(
        return_value={'textServiceError': 'false'})

    mocker.patch('aiohttp.ClientSession.get', mock_session_get)
    mocker.patch('aiohttp.ClientSession.post', mock_session_post)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session_get.assert_called_once()
    mock_session_post.assert_called_once()


@pytest.mark.asyncio
async def test_usps_track_no_tracking_info(mocker: MockerFixture) -> None:
    mock_session_get = mocker.MagicMock()
    mock_session_get.return_value.__aenter__.return_value.text = AsyncMock(
        return_value='could not locate the tracking information')
    mock_session_post = mocker.MagicMock()

    mocker.patch('aiohttp.ClientSession.get', mock_session_get)
    mocker.patch('aiohttp.ClientSession.post', mock_session_post)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session_get.assert_called_once()
    mock_session_post.assert_not_called()


@pytest.mark.asyncio
async def test_usps_track_text_service_error(mocker: MockerFixture) -> None:
    mock_session_get = mocker.MagicMock()
    mock_session_get.return_value.__aenter__.return_value.text = AsyncMock(
        return_value='tracking info')
    mock_session_post = mocker.MagicMock()
    mock_session_post.return_value.__aenter__.return_value.json = AsyncMock(
        return_value={'textServiceError': 'true'})

    mocker.patch('aiohttp.ClientSession.get', mock_session_get)
    mocker.patch('aiohttp.ClientSession.post', mock_session_post)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']

    with pytest.raises(TextServiceError):
        await usps_track(phone_number, tracking_numbers)

    mock_session_get.assert_called_once()
    mock_session_post.assert_called_once()


@pytest.mark.asyncio
async def test_usps_track_content_type_error(mocker: MockerFixture) -> None:
    mock_session_get = mocker.MagicMock()
    mock_session_get.return_value.__aenter__.return_value.text = AsyncMock(
        return_value='tracking info')
    mock_session_post = mocker.MagicMock()
    mock_session_post.return_value.__aenter__.return_value.json = AsyncMock(
        side_effect=ContentTypeError(mocker.MagicMock(), ()))

    mocker.patch('aiohttp.ClientSession.get', mock_session_get)
    mocker.patch('aiohttp.ClientSession.post', mock_session_post)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session_get.assert_called_once()
    mock_session_post.assert_called_once()

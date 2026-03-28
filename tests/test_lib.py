from __future__ import annotations

from json import JSONDecodeError
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock

from usps_track.lib import TextServiceError, usps_track
import pytest

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


@pytest.mark.asyncio
async def test_usps_track_success(mocker: MockerFixture) -> None:
    mock_response_get = MagicMock()
    mock_response_get.text = ''
    mock_response_post = MagicMock()
    mock_response_post.json.return_value = {'textServiceError': 'false'}
    mock_session = AsyncMock()
    mock_session.get.return_value = mock_response_get
    mock_session.post.return_value = mock_response_post
    mock_session.__aenter__.return_value = mock_session
    mocker.patch('usps_track.lib.niquests.AsyncSession', return_value=mock_session)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session.get.assert_called_once()
    mock_session.post.assert_called_once()


@pytest.mark.asyncio
async def test_usps_track_no_tracking_info(mocker: MockerFixture) -> None:
    mock_response_get = MagicMock()
    mock_response_get.text = 'could not locate the tracking information'
    mock_session = AsyncMock()
    mock_session.get.return_value = mock_response_get
    mock_session.__aenter__.return_value = mock_session
    mocker.patch('usps_track.lib.niquests.AsyncSession', return_value=mock_session)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session.get.assert_called_once()
    mock_session.post.assert_not_called()


@pytest.mark.asyncio
async def test_usps_track_text_service_error(mocker: MockerFixture) -> None:
    mock_response_get = MagicMock()
    mock_response_get.text = 'tracking info'
    mock_response_post = MagicMock()
    mock_response_post.json.return_value = {'textServiceError': 'true'}
    mock_session = AsyncMock()
    mock_session.get.return_value = mock_response_get
    mock_session.post.return_value = mock_response_post
    mock_session.__aenter__.return_value = mock_session
    mocker.patch('usps_track.lib.niquests.AsyncSession', return_value=mock_session)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']

    with pytest.raises(TextServiceError):
        await usps_track(phone_number, tracking_numbers)

    mock_session.get.assert_called_once()
    mock_session.post.assert_called_once()


@pytest.mark.asyncio
async def test_usps_track_content_type_error(mocker: MockerFixture) -> None:
    mock_response_get = MagicMock()
    mock_response_get.text = 'tracking info'
    mock_response_post = MagicMock()
    mock_response_post.json.side_effect = JSONDecodeError('', '', 0)
    mock_session = AsyncMock()
    mock_session.get.return_value = mock_response_get
    mock_session.post.return_value = mock_response_post
    mock_session.__aenter__.return_value = mock_session
    mocker.patch('usps_track.lib.niquests.AsyncSession', return_value=mock_session)

    phone_number = '123-456-7890'
    tracking_numbers = ['123456789012']
    await usps_track(phone_number, tracking_numbers)

    mock_session.get.assert_called_once()
    mock_session.post.assert_called_once()

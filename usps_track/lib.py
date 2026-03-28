"""Main library code for usps_track."""
from __future__ import annotations

from json import JSONDecodeError
from typing import TYPE_CHECKING, TypedDict, cast
import logging

import niquests

from .constants import (
    DEFAULT_STR_VALUE,
    HEADERS,
    URL_TRACK_CONFIRM_ACTION,
    URL_TRACK_CONFIRM_UPDATE,
)
from .utils import on_off

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ('TextServiceError', 'usps_track')

logger = logging.getLogger(__name__)


class ResponseDict(TypedDict):
    """Response dictionary from USPS text service."""
    textServiceError: str
    """Error string."""


class TextServiceError(Exception):
    """An error occurred with the USPS text service."""


async def usps_track(phone_number: str,
                     tracking_numbers: Iterable[str],
                     *,
                     confirm_sms: bool = True,
                     email: str = DEFAULT_STR_VALUE,
                     name: str = DEFAULT_STR_VALUE,
                     text_alert: bool = True,
                     text_all: bool = True,
                     text_dnd: bool = True,
                     text_future: bool = True,
                     text_oa: bool = True,
                     text_pickup: bool = True,
                     text_today: bool = True,
                     raise_for_status: bool = False) -> None:
    """
    Track a package using the USPS tracking system via SMS.

    Parameters
    ----------
    phone_number : str
        Must be a US phone number including area code without a leading '1-', and with each group
        separated using '-' as the delimiter.

    tracking_numbers : Iterable[str]
        Tracking numbers to track. USPS does generally accept international values, usually after
        the package gets into the US, but sometimes earlier than that (especially for Royal Mail).

    raise_for_status : bool
        Raise if any individual request fails.

    confirm_sms : bool

    email : str

    name : str

    text_alert : bool

    text_all : bool

    text_dnd : bool

    text_future : bool

    text_oa : bool

    text_pickup : bool

    text_today : bool

    Raises
    ------
    TextServiceError
        If the USPS text service returns an error.
    """
    async with niquests.AsyncSession(headers=HEADERS) as session:
        for number in tracking_numbers:
            r = await session.get(URL_TRACK_CONFIRM_ACTION, params={'qtc_tLabels1': number})
            if raise_for_status:
                r.raise_for_status()
            if 'could not locate the tracking information' in (r.text or ''):
                continue
            r2 = await session.post(URL_TRACK_CONFIRM_UPDATE,
                                    data={
                                        'confirmSms': on_off(confirm_sms),
                                        'email1': email,
                                        'label': number,
                                        'name1': name,
                                        'smsNumber': phone_number,
                                        'textAlert': on_off(text_alert),
                                        'textAll': on_off(text_all),
                                        'textDnd': on_off(text_dnd),
                                        'textFuture': on_off(text_future),
                                        'textOA': on_off(text_oa),
                                        'textPickup': on_off(text_pickup),
                                        'textToday': on_off(text_today)
                                    },
                                    headers={
                                        'Referer':
                                            f'{URL_TRACK_CONFIRM_ACTION}?qtc_tLabels1={number}',
                                        'X-Requested-With':
                                            'XMLHttpRequest'
                                    })
            if raise_for_status:
                r2.raise_for_status()
            try:
                if cast('ResponseDict', r2.json()).get('textServiceError') != 'false':
                    raise TextServiceError
            except JSONDecodeError:
                logger.debug('Error updating %s. Tracking number probably does not exist.', number)
                continue

"""Main library code for ``usps_track``."""
from __future__ import annotations

from json import JSONDecodeError
from typing import TYPE_CHECKING, Literal, TypedDict, cast
import logging

import niquests

from .constants import (
    DEFAULT_STR_VALUE,
    HEADERS,
    URL_TRACK_CONFIRM_ACTION,
    URL_TRACK_CONFIRM_UPDATE,
)

if TYPE_CHECKING:
    from collections.abc import Iterable

__all__ = ('TextServiceError', 'usps_track')

log = logging.getLogger(__name__)


def _on_off(
        val: bool) -> Literal['on', 'off']:  # ruff:ignore[boolean-type-hint-positional-argument]
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


class _ResponseDict(TypedDict):
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

    confirm_sms : bool
        Whether to confirm SMS enrolment.

    email : str
        Email address for notifications.

    name : str
        Name associated with the tracking request.

    text_alert : bool
        Enable text alerts.

    text_all : bool
        Enable all text notifications.

    text_dnd : bool
        Enable do-not-disturb override for texts.

    text_future : bool
        Enable future delivery text notifications.

    text_oa : bool
        Enable out-for-delivery text notifications.

    text_pickup : bool
        Enable pickup-available text notifications.

    text_today : bool
        Enable today's delivery text notifications.

    raise_for_status : bool
        Raise if any individual request fails.

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
                                        'confirmSms': _on_off(confirm_sms),
                                        'email1': email,
                                        'label': number,
                                        'name1': name,
                                        'smsNumber': phone_number,
                                        'textAlert': _on_off(text_alert),
                                        'textAll': _on_off(text_all),
                                        'textDnd': _on_off(text_dnd),
                                        'textFuture': _on_off(text_future),
                                        'textOA': _on_off(text_oa),
                                        'textPickup': _on_off(text_pickup),
                                        'textToday': _on_off(text_today)
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
                if cast('_ResponseDict', r2.json())['textServiceError'] != 'false':
                    raise TextServiceError
            except JSONDecodeError:
                log.debug('Error updating %s. Tracking number probably does not exist.', number)
                continue

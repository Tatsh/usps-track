from typing import Any, Iterable, TypedDict, cast
import logging

from aiohttp import TraceConfig
from aiohttp.client_exceptions import ContentTypeError
import aiohttp

from .constants import (DEFAULT_STR_VALUE, HEADERS, URL_TRACK_CONFIRM_ACTION,
                        URL_TRACK_CONFIRM_UPDATE)
from .utils import on_off

__all__ = ('TextServiceError', 'usps_track')

logger = logging.getLogger(__name__)


class ResponseDict(TypedDict):
    textServiceError: str


class TextServiceError(Exception):
    pass


async def usps_track(phone_number: str,
                     tracking_numbers: Iterable[str],
                     trace_configs: list[TraceConfig] | None = None,
                     raise_for_status: bool = False,
                     **kwargs: Any) -> None:
    """
    Parameters
    ----------

    phone_number : str
        Must be a US phone number including area code without a leading '1-', and with each group
        separated using '-' as the delimiter.

    tracking_numbers : Iterable[str]
        Tracking numbers to track. USPS does generally accept international values, usually after
        the package gets into the US, but sometimes earlier than that (especially for Royal Mail).

    trace_configs : list[TraceConfig] | None
        A list of ``aiohttp.TraceConfig`` instances.

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
    """
    async with aiohttp.ClientSession(headers=HEADERS, trace_configs=trace_configs) as session:
        for number in tracking_numbers:
            async with session.get(URL_TRACK_CONFIRM_ACTION,
                                   params=dict(qtc_tLabels1=number),
                                   raise_for_status=raise_for_status) as r:
                if 'could not locate the tracking information' in await r.text():
                    continue
                async with session.post(URL_TRACK_CONFIRM_UPDATE,
                                        data=dict(
                                            confirmSms=on_off(kwargs.get('confirm_sms', True)),
                                            email1=kwargs.get('email', DEFAULT_STR_VALUE),
                                            label=number,
                                            name1=kwargs.get('name', DEFAULT_STR_VALUE),
                                            smsNumber=phone_number,
                                            textAlert=on_off(kwargs.get('text_alert', True)),
                                            textAll=on_off(kwargs.get('text_all', True)),
                                            textDnd=on_off(kwargs.get('text_dnd', True)),
                                            textFuture=on_off(kwargs.get('text_future', True)),
                                            textOA=on_off(kwargs.get('text_oa', True)),
                                            textPickup=on_off(kwargs.get('text_pickup', True)),
                                            textToday=on_off(kwargs.get('text_today', True)),
                                        ),
                                        headers={
                                            'Referer':
                                                f'{URL_TRACK_CONFIRM_ACTION}?qtc_tLabels1={number}',
                                            'X-Requested-With':
                                                'XMLHttpRequest',
                                        },
                                        raise_for_status=raise_for_status) as r2:
                    try:
                        if cast(ResponseDict, await r2.json()).get('textServiceError') != 'false':
                            raise TextServiceError()
                    except ContentTypeError:
                        logger.debug('Error updating %s. Tracking number probably does not exist.',
                                     number)
                        continue

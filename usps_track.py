#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from os.path import basename
from types import SimpleNamespace
from typing import (Any, Final, Iterable, List, Literal, Optional, Sequence,
                    TypedDict, cast)
import argparse
import asyncio
import logging
import sys

from aiohttp import TraceConfig
from aiohttp.client_exceptions import ContentTypeError
from aiohttp.tracing import TraceRequestStartParams
from aiohttp.typedefs import LooseHeaders
import aiohttp
import argcomplete

__all__ = ('usps_track',)

URL_PREFIX: Final[str] = 'https://tools.usps.com/go'
URL_TRACK_CONFIRM_ACTION: Final[str] = (f'{URL_PREFIX}/TrackConfirmAction')
URL_TRACK_CONFIRM_UPDATE: Final[str] = (
    f'{URL_PREFIX}/TrackConfirmRequestUpdateAJAXAction.action')
DEFAULT_STR_VALUE: Final[str] = 'not required'
HEADERS: Final[LooseHeaders] = {
    'Accept':
    'text/html,application/xhtml+xml,'
    'application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':
    'en-US,en;q=0.8,en-GB;q=0.6',
    'Cache-Control':
    'no-cache',
    'Connection':
    'keep-alive',
    'DNT':
    '1',
    'Pragma':
    'no-cache',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/66.0.3359.45 '
    'Safari/537.36'
}


class ResponseDict(TypedDict):
    textServiceError: str


async def on_off(val: bool) -> Literal['on', 'off']:
    return 'on' if val else 'off'


async def usps_track(phone_number: str,
                     tracking_numbers: Iterable[str],
                     trace_configs: Optional[List[TraceConfig]] = None,
                     raise_for_status: bool = False,
                     **kwargs: Any) -> int:
    """
    Args
    ----

    phone_number
    Must be a US phone number including area code without a leading '1-', and
    with each group separated using '-' as the delimiter.

    tracking_numbers
    Tracking numbers to track. USPS does generally accept international values,
    usually after the package gets into the US, but sometimes earlier than
    that (especially for Royal Mail).

    trace_configs
    A list of ``aiohttp.TraceConfig`` instances.

    raise_for_status
    Raise if any individual request fails.

    confirm_sms
    email
    name
    text_alert
    text_all
    text_dnd
    text_future
    text_oa
    text_pickup
    text_today

    Returns 0 if all requests were successful, 1 if one or more failed.
    """
    ret = 0
    async with aiohttp.ClientSession(headers=HEADERS,
                                     trace_configs=trace_configs) as session:
        for number in tracking_numbers:
            async with session.get(URL_TRACK_CONFIRM_ACTION,
                                   params=dict(qtc_tLabels1=number),
                                   raise_for_status=raise_for_status) as r:
                if ('could not locate the tracking information' in await
                        r.text()):
                    continue
                async with session.post(
                        URL_TRACK_CONFIRM_UPDATE,
                        data=dict(
                            confirmSms=await on_off(
                                kwargs.get('confirm_sms', True)),
                            email1=kwargs.get('email', DEFAULT_STR_VALUE),
                            label=number,
                            name1=kwargs.get('name', DEFAULT_STR_VALUE),
                            smsNumber=phone_number,
                            textAlert=await on_off(
                                kwargs.get('text_alert', True)),
                            textAll=await on_off(kwargs.get('text_all', True)),
                            textDnd=await on_off(kwargs.get('text_dnd', True)),
                            textFuture=await on_off(
                                kwargs.get('text_future', True)),
                            textOA=await on_off(kwargs.get('text_oa', True)),
                            textPickup=await on_off(
                                kwargs.get('text_pickup', True)),
                            textToday=await on_off(
                                kwargs.get('text_today', True)),
                        ),
                        headers={
                            'Referer':
                            f'{URL_TRACK_CONFIRM_ACTION}?qtc_tLabels1={number}',
                            'X-Requested-With': 'XMLHttpRequest',
                        },
                        raise_for_status=raise_for_status) as r2:
                    try:
                        if ((cast(ResponseDict, await
                                  r2.json())).get('textServiceError') !=
                                'false'):
                            ret = 1
                    except ContentTypeError:
                        ret = 1
    return ret


class Namespace(argparse.Namespace):
    debug: bool
    phone_number: Sequence[str]
    tracking_number: Sequence[str]


async def on_request_start(_session: aiohttp.ClientSession,
                           _trace_config_ctx: SimpleNamespace,
                           params: TraceRequestStartParams) -> None:
    asyncio.get_running_loop().run_in_executor(
        None, print, f'DEBUG:aiohttp:{params.method} {params.url}')


def main() -> int:
    name = basename(sys.argv[0])
    parser = argparse.ArgumentParser(name)
    parser.add_argument('tracking_number',
                        nargs='+',
                        metavar='TRACKING_NUMBER',
                        help='Tracking numbers')
    parser.add_argument('phone_number',
                        nargs=1,
                        metavar='PHONE_NUMBER',
                        help='Phone number to send SMS to (US only)')
    parser.add_argument('-d', '--debug', action='store_true')
    if argcomplete:
        argcomplete.autocomplete(parser)
    args = cast(Namespace, parser.parse_args())
    log = logging.getLogger(name)
    trace_configs = []
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        trace_config = TraceConfig()
        trace_config.on_request_start.append(on_request_start)
        trace_configs.append(trace_config)
    phone_number = args.phone_number[0]
    if '-' not in phone_number:
        if phone_number[0] == '1' and len(phone_number) == 11:
            phone_number = phone_number[1:]
            log.debug('Removed leading 1')
        parts = [phone_number[i:i + 3] for i in range(0, 10, 3)]
        log.debug('Phone number parts: %s', parts)
        phone_number = '-'.join(parts[0:3]) + parts[3]
        log.debug('Adjusted phone number: %s', phone_number)
    return asyncio.run(
        usps_track(phone_number,
                   args.tracking_number,
                   trace_configs,
                   raise_for_status=True))


if __name__ == '__main__':
    main()

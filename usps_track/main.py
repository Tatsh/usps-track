from types import SimpleNamespace
import asyncio
import logging

from aiohttp import TraceConfig
from aiohttp.tracing import TraceRequestStartParams
import aiohttp
import click

from .constants import US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH
from .lib import usps_track

__all__ = ('main',)

log = logging.getLogger(__name__)


async def on_request_start(  # pragma: no cover # noqa: RUF029
        _session: aiohttp.ClientSession, _trace_config_ctx: SimpleNamespace,
        params: TraceRequestStartParams) -> None:
    asyncio.get_running_loop().run_in_executor(None, log.debug, f'{params.method} {params.url}')


@click.command('usps-track')
@click.argument('tracking_numbers', metavar='TRACKING_NUMBER', nargs=-1)
@click.argument('phone_number', metavar='PHONE_NUMBER', nargs=1)
@click.option('-d', '--debug', is_flag=True, help='Enable debug logging.')
def main(phone_number: str, tracking_numbers: tuple[str, ...], *, debug: bool = False) -> None:
    logging.basicConfig(level=logging.DEBUG if debug else logging.ERROR)
    trace_configs = []
    if debug:
        trace_config = TraceConfig()
        trace_config.on_request_start.append(on_request_start)
        trace_configs.append(trace_config)
    if '-' not in phone_number:
        if phone_number[0] == '1' and len(phone_number) == US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH:
            phone_number = phone_number[1:]
            log.debug('Removed leading 1.')
        parts = [phone_number[i:i + 3] for i in range(0, 10, 3)]
        phone_number = '-'.join(parts[0:3]) + parts[3]
        log.debug('Adjusted phone number.')
    asyncio.run(usps_track(phone_number, tracking_numbers, trace_configs, raise_for_status=True),
                debug=debug)

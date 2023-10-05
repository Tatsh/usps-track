from types import SimpleNamespace
import asyncio

from aiohttp import TraceConfig
from aiohttp.tracing import TraceRequestStartParams
from loguru import logger
import aiohttp
import click

from .lib import usps_track
from .utils import setup_logging

__all__ = ('main',)


async def on_request_start(_session: aiohttp.ClientSession, _trace_config_ctx: SimpleNamespace,
                           params: TraceRequestStartParams) -> None:
    asyncio.get_running_loop().run_in_executor(None, logger.debug, f'{params.method} {params.url}')


@click.command('usps-track')
@click.argument('tracking_numbers', metavar='TRACKING_NUMBER', nargs=-1)
@click.argument('phone_number', metavar='PHONE_NUMBER', nargs=1)
@click.option('-d', '--debug', is_flag=True, help='Enable debug logging.')
def main(phone_number: str, tracking_numbers: list[str], debug: bool = False) -> None:
    setup_logging(debug)
    trace_configs = []
    if debug:
        trace_config = TraceConfig()
        trace_config.on_request_start.append(on_request_start)
        trace_configs.append(trace_config)
    phone_number = phone_number
    if '-' not in phone_number:
        if phone_number[0] == '1' and len(phone_number) == 11:
            phone_number = phone_number[1:]
            logger.debug('Removed leading 1')
        parts = [phone_number[i:i + 3] for i in range(0, 10, 3)]
        logger.debug(f'Phone number parts: {parts}')
        phone_number = '-'.join(parts[0:3]) + parts[3]
        logger.debug(f'Adjusted phone number: {phone_number}')
    asyncio.run(usps_track(phone_number, tracking_numbers, trace_configs, raise_for_status=True),
                debug=debug)

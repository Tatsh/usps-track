"""CLI entry point."""
from __future__ import annotations

import asyncio
import logging

from bascom import setup_logging
import click

from .constants import US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH
from .lib import usps_track

__all__ = ('main',)

log = logging.getLogger(__name__)


@click.command('usps-track', context_settings={'help_option_names': ('-h', '--help')})
@click.argument('tracking_numbers', metavar='TRACKING_NUMBER', nargs=-1)
@click.argument('phone_number', metavar='PHONE_NUMBER', nargs=1)
@click.option('-d', '--debug', is_flag=True, help='Enable debug logging.')
def main(phone_number: str, tracking_numbers: tuple[str, ...], *, debug: bool = False) -> None:
    """Track USPS packages using tracking numbers and phone number."""
    setup_logging(debug=debug,
                  loggers={
                      'usps_track': {
                          'handlers': ('console',),
                          'level': logging.DEBUG if debug else logging.INFO,
                          'propagate': False,
                      }
                  })
    if '-' not in phone_number:
        if phone_number[0] == '1' and len(phone_number) == US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH:
            phone_number = phone_number[1:]
            log.debug('Removed leading 1.')
        parts = [phone_number[i:i + 3] for i in range(0, 10, 3)]
        phone_number = '-'.join(parts[0:3]) + parts[3]
        log.debug('Adjusted phone number.')
    asyncio.run(usps_track(phone_number, tracking_numbers, raise_for_status=True), debug=debug)

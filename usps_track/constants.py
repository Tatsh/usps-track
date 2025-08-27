"""Constants."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp.typedefs import LooseHeaders

__all__ = ('DEFAULT_STR_VALUE', 'HEADERS', 'URL_PREFIX', 'URL_TRACK_CONFIRM_ACTION',
           'URL_TRACK_CONFIRM_UPDATE', 'US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH')

DEFAULT_STR_VALUE = 'not required'
"""Default value for optional string parameters."""
HEADERS: LooseHeaders = {
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
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
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36'
                   '(KHTML, like Gecko) Chrome/66.0.3359.45 Safari/537.36')
}
"""HTTP headers to use for requests."""
URL_PREFIX = 'https://tools.usps.com/go'
"""Base URL for USPS tracking tools."""
URL_TRACK_CONFIRM_ACTION = f'{URL_PREFIX}/TrackConfirmAction'
"""URL for USPS tracking confirmation action."""
URL_TRACK_CONFIRM_UPDATE = f'{URL_PREFIX}/TrackConfirmRequestUpdateAJAXAction.action'
"""URL for USPS tracking confirmation update AJAX action."""
US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH = 11
"""Length of a US phone number with a leading '1'."""

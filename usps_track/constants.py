"""Constants."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp.typedefs import LooseHeaders

__all__ = ('DEFAULT_STR_VALUE', 'HEADERS', 'URL_PREFIX', 'URL_TRACK_CONFIRM_ACTION',
           'URL_TRACK_CONFIRM_UPDATE', 'US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH')

DEFAULT_STR_VALUE = 'not required'
"""
Default value for optional string parameters.

:meta hide-value:
"""
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
                   '(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
}
"""
HTTP headers to use for requests.

:meta hide-value:
"""
URL_PREFIX = 'https://tools.usps.com/go'
"""
Base URL for USPS tracking tools.

:meta hide-value:
"""
URL_TRACK_CONFIRM_ACTION = f'{URL_PREFIX}/TrackConfirmAction'
"""
URL for USPS tracking confirmation action.

:meta hide-value:
"""
URL_TRACK_CONFIRM_UPDATE = f'{URL_PREFIX}/TrackConfirmRequestUpdateAJAXAction.action'
"""
URL for USPS tracking confirmation update AJAX action.

:meta hide-value:
"""
US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH = 11
"""
Length of a US phone number with a leading '1'.

:meta hide-value:
"""

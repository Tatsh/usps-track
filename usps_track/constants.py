from aiohttp.typedefs import LooseHeaders

__all__ = ('DEFAULT_STR_VALUE', 'HEADERS', 'URL_PREFIX', 'URL_TRACK_CONFIRM_ACTION',
           'URL_TRACK_CONFIRM_UPDATE', 'US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH')

DEFAULT_STR_VALUE = 'not required'
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
URL_PREFIX = 'https://tools.usps.com/go'
URL_TRACK_CONFIRM_ACTION = f'{URL_PREFIX}/TrackConfirmAction'
URL_TRACK_CONFIRM_UPDATE = f'{URL_PREFIX}/TrackConfirmRequestUpdateAJAXAction.action'
US_PHONE_NUMBER_WITH_LEADING_ONE_LENGTH = 11

# usps-track

Quickly track via SMS several USPS (and some international) tracking numbers via the command line.

For international to work, the destination country must be USA.

The phone number argument must be a US phone number.

## Usage

```plain
usage: usps_track.py [-h] TRACKING_NUMBER [TRACKING_NUMBER ...] PHONE_NUMBER

positional arguments:
  TRACKING_NUMBER  Tracking numbers
  PHONE_NUMBER     Phone number to send SMS to (US only)
```

This can also be used as a library:

```python
from usps_track import usps_track

async def usage():
    await usps_track('555-555-5555',
                     ['tracking_number_1'],
                     raise_for_status=True)
```

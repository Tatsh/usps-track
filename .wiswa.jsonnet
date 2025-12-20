local utils = import 'utils.libjsonnet';

{
  description: 'Quickly track via SMS several USPS (and some international) tracking numbers via the command line.',
  keywords: ['command line', 'shipping', 'usps'],
  project_name: 'usps-track',
  version: '0.0.3',
  want_main: true,
  citation+: {
    'date-released': '2025-08-27',
  },
  copilot+: {
    intro: 'usps-track is a command line tool to track USPS packages via SMS.',
  },
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          aiohttp: utils.latestPypiPackageVersionCaret('aiohttp'),
        },
        group+: {
          tests+: {
            dependencies+: {
              'pytest-asyncio': utils.latestPypiPackageVersionCaret('pytest-asyncio'),
            },
          },
        },
      },
    },
  },
}

local utils = import 'utils.libjsonnet';

{
  uses_user_defaults: true,
  description: 'Quickly track via SMS several USPS (and some international) tracking numbers via the command line.',
  keywords: ['command line', 'shipping', 'usps'],
  project_name: 'usps-track',
  version: '0.0.5',
  want_main: true,
  want_flatpak: true,
  publishing+: { flathub: 'sh.tat.usps-track' },
  snapcraft+: {
    summary: 'Quickly track USPS and international packages via the command line.',
  },
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          niquests: utils.latestPypiPackageVersionCaret('niquests'),
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

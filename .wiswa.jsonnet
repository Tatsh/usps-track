local utils = import 'utils.libjsonnet';

(import 'defaults.libjsonnet') + {
  // Project-specific
  description: 'Quickly track via SMS several USPS (and some international) tracking numbers via the command line.',
  keywords: ['command line', 'shipping', 'usps'],
  project_name: 'usps-track',
  version: '0.0.2',
  want_main: true,
  citation+: {
    'date-released': '2025-08-27',
  },
  pyproject+: {
    tool+: {
      poetry+: {
        dependencies+: {
          aiohttp: '^3.12.15',
        },
        group+: {
          tests+: {
            dependencies+: {
              'pytest-asyncio': '^1.1.0',
            },
          },
        },
      },
    },
  },
  // Common
  authors: [
    {
      'family-names': 'Udvare',
      'given-names': 'Andrew',
      email: 'audvare@gmail.com',
      name: '%s %s' % [self['given-names'], self['family-names']],
    },
  ],
  local funding_name = '%s2' % std.asciiLower(self.github_username),
  github_username: 'Tatsh',
  social+: {
    mastodon+: { id: '109370961877277568' },
  },
  github+: {
    funding+: {
      ko_fi: funding_name,
      liberapay: funding_name,
      patreon: funding_name,
    },
  },
  docs_conf+: {
    config+: {
      intersphinx_mapping+: {
        aiohttp: ['https://docs.aiohttp.org/en/stable/', null],
      },
    },
  },
}

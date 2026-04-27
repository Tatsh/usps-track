# usps-track

<!-- WISWA-GENERATED-README:START -->

[![Python versions](https://img.shields.io/pypi/pyversions/usps-track.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/usps-track)](https://pypi.org/project/usps-track/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/tags)
[![License](https://img.shields.io/github/license/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/usps-track/v0.0.5/master)](https://github.com/Tatsh/usps-track/compare/v0.0.5...master)
[![CodeQL](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/usps-track/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/usps-track?branch=master)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://github.com/dependabot)
[![Documentation Status](https://readthedocs.org/projects/usps-track/badge/?version=latest)](https://usps-track.readthedocs.org/?badge=latest)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![uv](https://img.shields.io/badge/uv-261230?logo=astral)](https://docs.astral.sh/uv/)
[![pytest](https://img.shields.io/badge/pytest-zz?logo=Pytest&labelColor=black&color=black)](https://docs.pytest.org/en/stable/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/usps-track/month)](https://pepy.tech/project/usps-track)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/usps-track?logo=github&style=flat)](https://github.com/Tatsh/usps-track/stargazers)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Prettier](https://img.shields.io/badge/Prettier-black?logo=prettier)](https://prettier.io/)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor=did%3Aplc%3Auq42idtvuccnmtl57nsucz72&query=%24.followersCount&label=Follow+%40Tatsh&logo=bluesky&style=social)](https://bsky.app/profile/Tatsh.bsky.social)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Tatsh-black?logo=buymeacoffee)](https://buymeacoffee.com/Tatsh)
[![Libera.Chat](https://img.shields.io/badge/Libera.Chat-Tatsh-black?logo=liberadotchat)](irc://irc.libera.chat/Tatsh)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)
[![Patreon](https://img.shields.io/badge/Patreon-Tatsh2-F96854?logo=patreon)](https://www.patreon.com/Tatsh2)

<!-- WISWA-GENERATED-README:STOP -->

Quickly track via SMS several USPS (and some international) tracking numbers via the command line.

## Installation

```shell
pip install usps-track
```

## Usage

Add `-d` to show debug logs.

```shell
Usage: usps-track [OPTIONS] TRACKING_NUMBER PHONE_NUMBER

  Track USPS packages using tracking numbers and phone number.

Options:
  -d, --debug  Enable debug logging.
  -h, --help   Show this message and exit.
```

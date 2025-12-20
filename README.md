# usps-track

[![Python versions](https://img.shields.io/pypi/pyversions/usps-track.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/usps-track)](https://pypi.org/project/usps-track/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/tags)
[![License](https://img.shields.io/github/license/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/usps-track/v0.0.3/master)](https://github.com/Tatsh/usps-track/compare/v0.0.3...master)
[![CodeQL](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/usps-track/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/usps-track?branch=master)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://github.com/dependabot)
[![Documentation Status](https://readthedocs.org/projects/usps-track/badge/?version=latest)](https://usps-track.readthedocs.org/?badge=latest)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Poetry](https://img.shields.io/badge/Poetry-242d3e?logo=poetry)](https://python-poetry.org)
[![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-AD4CD3?logo=pydocstyle)](https://www.pydocstyle.org/)
[![pytest](https://img.shields.io/badge/pytest-enabled-CFB97D?logo=pytest)](https://docs.pytest.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/usps-track/month)](https://pepy.tech/project/usps-track)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/usps-track?logo=github&style=flat)](https://github.com/Tatsh/usps-track/stargazers)
[![Prettier](https://img.shields.io/badge/Prettier-enabled-black?logo=prettier)](https://prettier.io/)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor=did%3Aplc%3Auq42idtvuccnmtl57nsucz72&query=%24.followersCount&style=social&logo=bluesky&label=Follow+%40Tatsh)](https://bsky.app/profile/Tatsh.bsky.social)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Tatsh-black?logo=buymeacoffee)](https://buymeacoffee.com/Tatsh)
[![Libera.Chat](https://img.shields.io/badge/Libera.Chat-Tatsh-black?logo=liberadotchat)](irc://irc.libera.chat/Tatsh)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)
[![Patreon](https://img.shields.io/badge/Patreon-Tatsh2-F96854?logo=patreon)](https://www.patreon.com/Tatsh2)

Quickly track via SMS several USPS (and some international) tracking numbers via the command line.

## Installation

### Poetry

```shell
poetry add usps-track
```

### Pip

```shell
pip install usps-track
```

## Usage

Add `-d` to show debug logs.

```shell
usps-track TRACKING_NUMBER PHONE_NUMBER
```

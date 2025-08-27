# usps-track

[![Python versions](https://img.shields.io/pypi/pyversions/usps-track.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/usps-track)](https://pypi.org/project/usps-track/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/tags)
[![License](https://img.shields.io/github/license/Tatsh/usps-track)](https://github.com/Tatsh/usps-track/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/usps-track/v0.0.2/master)](https://github.com/Tatsh/usps-track/compare/v0.0.2...master)
[![CodeQL](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/usps-track/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/usps-track/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/usps-track?branch=master)
[![Documentation Status](https://readthedocs.org/projects/usps-track/badge/?version=latest)](https://usps-track.readthedocs.org/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/usps-track/month)](https://pepy.tech/project/usps-track)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/usps-track?logo=github&style=flat)](https://github.com/Tatsh/usps-track/stargazers)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor%3Ddid%3Aplc%3Auq42idtvuccnmtl57nsucz72%26query%3D%24.followersCount%26style%3Dsocial%26logo%3Dbluesky%26label%3DFollow%2520%40Tatsh&query=%24.followersCount&style=social&logo=bluesky&label=Follow%20%40Tatsh)](https://bsky.app/profile/Tatsh.bsky.social)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)

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

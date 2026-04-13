# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.1/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Changed

- Inlined `on_off` utility into `lib` module as a private `_on_off` function.
- Renamed `ResponseDict` to `_ResponseDict` to reflect its private usage.
- Renamed `logger` to `log` in `lib` module.
- Use dict key access instead of `.get()` for `textServiceError` response field.

### Removed

- `usps_track.utils` module (functionality moved into `lib`).
- `tests/test_utils.py` (no longer needed after removing `utils` module).

## [0.0.4] - 2026-03-28

### Added

- `-h` as a short alias for `--help`.

### Changed

- Switched to niquests library.

## [0.0.3] - 2025-12-20

### Added

- Attestation.

## [0.0.2] - 2025-04-12

Maintenance release.

## [0.0.1] - 2020-11-10

First version.

[unreleased]: https://github.com/Tatsh/usps-track/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/Tatsh/usps-track/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/Tatsh/usps-track/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/Tatsh/usps-track/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/Tatsh/usps-track/releases/tag/v0.0.1

"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import markmaple


def test_version_is_set() -> None:
    assert markmaple.__version__

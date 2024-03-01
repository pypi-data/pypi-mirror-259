from __future__ import annotations

import importlib.metadata

import zfit_astro as m


def test_version():
    assert importlib.metadata.version("zfit_astro") == m.__version__

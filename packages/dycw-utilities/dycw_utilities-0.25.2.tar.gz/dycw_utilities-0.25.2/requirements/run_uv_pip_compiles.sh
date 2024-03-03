#!/usr/bin/env bash

packages=(
    atomicwrites
    beartype
    bs4
    cacher
    cachetools
    click
    cryptography
    cvxpy
    fastapi
    fpdf2
    hatch
    holoviews
    ipython
    jupyter
    loguru
    luigi
    memory-profiler
    more-itertools
    numpy
    pandas
    pathvalidate
    polars
    pqdm
    pydantic
    pyinstrument
    pytest-check
    scipy
    scripts-clean-dir
    scripts-csv-to-markdown
    scripts-generate-snippets
    scripts-luigi-server
    scripts-monitor-memory
    scripts-pypi-server
    semver
    sqlalchemy
    sqlalchemy-polars
    typed-settings
    xarray
    xlrd
    zarr
)
for package in "${packages[@]}"; do
    uv pip compile \
        "--extra=${package}" \
        "--extra=zzz-test-${package}" \
        "--extra=test" \
        --quiet \
        --prerelease=disallow \
        "--output-file=requirements/${package}.txt" \
        --upgrade \
        --python-version=3.10 \
        pyproject.toml
done

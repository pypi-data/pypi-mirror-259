import os

from setuptools import setup

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="campuspulse-event-ingest-schema",
    description="Normalized data schema for the output of the data-ingest pipeline.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Adrian Edwards",
    url="https://github.com/CampusPulse/event-data-schema",
    project_urls={
        "Issues": "https://github.com/CampusPulse/event-data-schema/issues",
        "CI": "https://github.com/CampusPulse/event-data-schema/actions",
        "Changelog": "https://github.com/CampusPulse/event-data-schema/releases",
    },
    license="MIT",
    version=VERSION,
    packages=["campuspulse_event_ingest_schema"],
    install_requires=["pydantic[email]~=1.10"],
    extras_require={"test": ["pytest"], "lint": ["flake8", "black", "mypy", "isort"]},
    tests_require=["campuspulse-event-ingest-schema[test]"],
    python_requires=">=3.8",
)

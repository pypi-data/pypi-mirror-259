from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="satosacontrib.perun",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/perun/perun-proxyidp/satosacontrib-perun.git",
    description="Microservices, backends and add-ons for SATOSA authentication proxy",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "SATOSA~=8.1",
        "pysaml2~=7.1",
        "requests~=2.28",
        "perun.connector~=3.8",
        "PyYAML~=6.0",
        "SQLAlchemy~=2.0",
        "jwcrypto~=1.3",
        "natsort~=8.4.0",
        "python-dateutil~=2.8",
        "geoip2~=4.6",
        "user_agents~=2.2",
        "pymongo>=3.13.0,<5",  # for compatibility with proxyidp-gui
    ],
)

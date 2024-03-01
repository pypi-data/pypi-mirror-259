import os
import sys
import setuptools
from setuptools import find_packages, setup




def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError('Unable to find version string.')


version = get_version('fluent_formatter/__init__.py')




with open('README.md', 'r') as fh:
    long_description = fh.read()

description = (
    'A Python log formatter for use with fluent-logger-python. '
    'Formats datetime objects into ISO 8601 strings.'
)

setuptools.setup(
    name='python-fluent-log-formatter',
    version=version,
    author='Armandt van Zyl',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.8',
    install_requires=[
        'fluent-logger',
        'msgpack',
    ],
)

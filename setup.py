from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'opentok',
    version = find_version('opentok', '__init__.py'),
    description = 'OpenTok server-side SDK',
    long_description=long_description,

    url = 'https://github.com/opentok/Opentok-Python-SDK',

    author='TokBox, Inc.',
    author_email='support@tokbox.com',
    license='MIT',

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',

        'License :: OSI Approved :: MIT License',

        # TODO: verify that the package actually works in all these versions
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',

        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Conferencing',
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    keywords = 'video chat tokbox tok opentok python media webrtc archiving realtime',

    packages=find_packages(exclude=["contrib", "docs", "tests*"]),

    install_requires=[
        'requests>=1,<2',
        'enum34'
    ],

    # TODO: these aren't in the sample package, but might again become imp
    #       if JSON schema files are needed
    # zip_safe = False,
    # include_package_data = True,

    # NOTE: this isn't included in the sample packaging recommendation, but it seems to be the 
    #       de-facto standard for testing tools, Travis uses nose
    test_suite='nose.collector',
    tests_require=[
        'nose'
    ],
)

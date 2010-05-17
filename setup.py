#!/usr/bin/env python

# pyutil -- utility functions and classes
#
# Author: Zooko Wilcox-O'Hearn
#
# See README.txt for licensing information.

import os, re, sys

try:
    from ez_setup import use_setuptools
except ImportError:
    pass
else:
    use_setuptools(download_delay=0)

from setuptools import find_packages, setup

trove_classifiers=[
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    ]

PKG='pyutil'
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))

setup_requires = []

# darcsver is needed only if you want "./setup.py darcsver" to write a new
# version stamp in pyutil/_version.py, with a version number derived from
# darcs history.  http://pypi.python.org/pypi/darcsver
if 'darcsver' in sys.argv[1:]:
    setup_requires.append('darcsver >= 1.0.0')

# setuptools_darcs is required to produce complete distributions (such as with
# "sdist" or "bdist_egg"), unless there is a pyutil.egg-info/SOURCE.txt file
# present which contains a complete list of files that should be included.
# http://pypi.python.org/pypi/setuptools_darcs
setup_requires.append('setuptools_darcs >= 1.1.0')

data_fnames=[ 'COPYING.GPL', 'COPYING.TGPPL.html', 'README.txt', 'CREDITS' ]

# In case we are building for a .deb with stdeb's sdist_dsc command, we put the
# docs in "share/doc/python-$PKG".
doc_loc = "share/doc/" + PKG
data_files = [(doc_loc, data_fnames)]

def _setup(test_suite):
    setup(name=PKG,
          version=verstr,
          description='a collection of mature utilities for Python programmers',
          long_description="These are a few data structures, classes and functions which we've needed over many years of Python programming and which seem to be of general use to other Python programmers.  Many of the modules that have existed in pyutil over the years have subsequently been obsoleted by new features added to the Python language or its standard library, thus showing that we're not alone in wanting tools like these.",
          author='Zooko O\'Whielacronx',
          author_email='zooko@zooko.com',
          url='http://tahoe-lafs.org/trac/' + PKG,
          license='GNU GPL', # see README.txt for details -- there is also an alternative licence
          packages=find_packages(),
          include_package_data=True,
          setup_requires=setup_requires,
          install_requires=['argparse >= 0.8', 'zbase32 >= 1.0', 'simplejson >= 2.1.0'],
          classifiers=trove_classifiers,
          entry_points = {
              'console_scripts': [
                  'randcookie = pyutil.scripts.randcookie:main',
                  'tailx = pyutil.scripts.tailx:main',
                  'lines = pyutil.scripts.lines:main',
                  'randfile = pyutil.scripts.randfile:main',
                  'unsort = pyutil.scripts.unsort:main',
                  'verinfo = pyutil.scripts.verinfo:main',
                  ] },
          test_suite=test_suite,
          zip_safe=False, # I prefer unzipped for easier access.
          )

test_suite_name=PKG+".test"
try:
    _setup(test_suite=test_suite_name)
except Exception, le:
    # to work around a bug in Elisa v0.3.5
    # https://bugs.launchpad.net/elisa/+bug/263697
    if "test_suite must be a list" in str(le):
        _setup(test_suite=[test_suite_name])
    else:
        raise

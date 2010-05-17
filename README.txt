pyutil -- a library of useful Python functions and classes

Many of these utilities (or their ancestors) were developed for the Mojo Nation
open source project, its open source successor project Mnet, its proprietary
successor project Allmydata.com "Mountain View", or its open source successor
project Allmydata.org "Tahoe".  (In the case where the code was developed for a
for-profit company, the copyright holder donated the pyutil code to the public
under these open source licences.)

trac:

http://allmydata.org/trac/pyutil

darcs repository:

http://allmydata.org/source/pyutil/trunk

To run tests, do

python ./setup.py test

Some modules have self-benchmarks provided.  For example, to benchmark
the cache module, do

python -OOu -c 'from pyutil.test import test_cache; test_cache.quick_bench()'

or for more complete and time-consuming results:

python -OOu -c 'from pyutil.test import test_cache; test_cache.slow_bench()'

(The "-O" is important when benchmarking, since cache has extensive
self-tests that are optimized out when -O is included.)


LICENCE

You may use this package under the GNU General Public License, version 2 or, at
your option, any later version.  You may use this package under the Transitive
Grace Period Public Licence, version 1.0, or at your option, any later version.
(You may choose to use this package under the terms of either licence, at your
option.)  See the file COPYING.GPL for the terms of the GNU General Public
License, version 2.  See the file COPYING.TGPPL.html for the terms of the
Transitive Grace Period Public Licence, version 1.0.

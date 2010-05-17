#!/usr/bin/env python

try:
    from twisted.trial import unittest
except ImportError, le:
    print "Skipping test_iputil since it requires Twisted and Twisted could not be imported: %s" % (le,)
else:
    from pyutil import iputil, testutil
    import re, sys

    DOTTED_QUAD_RE=re.compile("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$")

    class ListAddresses(testutil.SignalMixin):
        def test_get_local_ip_for(self):
            addr = iputil.get_local_ip_for('127.0.0.1')
            self.failUnless(DOTTED_QUAD_RE.match(addr))

        def test_list_async(self):
            try:
                from twisted.trial import unittest
                from pyutil import iputil, testutil
            except ImportError, le:
                raise SkipTest("iputil could not be imported (probably because its dependency, Twisted, is not installed).  %s" % (le,))

            d = iputil.get_local_addresses_async()
            def _check(addresses):
                self.failUnless(len(addresses) >= 1) # always have localhost
                self.failUnless("127.0.0.1" in addresses, addresses)
            d.addCallbacks(_check)
            return d
        test_list_async.timeout=2

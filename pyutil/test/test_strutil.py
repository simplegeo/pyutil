#!/usr/bin/env python

# Copyright (c) 2004-2009 Zooko "Zooko" Wilcox-O'Hearn
#  This file is part of pyutil; see README.txt for licensing terms.

import unittest

from pyutil.assertutil import _assert, precondition, postcondition
from pyutil.humanreadable import hr
from pyutil.strutil import *

class Teststrutil(unittest.TestCase):
    def test_short_input(self):
        self.failUnless(pop_trailing_newlines("\r\n") == "")
        self.failUnless(pop_trailing_newlines("\r") == "")
        self.failUnless(pop_trailing_newlines("x\r\n") == "x")
        self.failUnless(pop_trailing_newlines("x\r") == "x")

    def test_split(self):
        _assert(split_on_newlines("x\r\ny") == ["x", "y",], split_on_newlines("x\r\ny"))
        _assert(split_on_newlines("x\r\ny\r\n") == ["x", "y", '',], split_on_newlines("x\r\ny\r\n"))
        _assert(split_on_newlines("x\n\ny\n\n") == ["x", '', "y", '', '',], split_on_newlines("x\n\ny\n\n"))

    def test_commonprefix(self):
        _assert(commonprefix(["foo","foobarooo", "foosplat",]) == 'foo', commonprefix(["foo","foobarooo", "foosplat",]))
        _assert(commonprefix(["foo","afoobarooo", "foosplat",]) == '', commonprefix(["foo","afoobarooo", "foosplat",]))

    def test_commonsuffix(self):
        _assert(commonsuffix(["foo","foobarooo", "foosplat",]) == '', commonsuffix(["foo","foobarooo", "foosplat",]))
        _assert(commonsuffix(["foo","foobarooo", "foosplato",]) == 'o', commonsuffix(["foo","foobarooo", "foosplato",]))
        _assert(commonsuffix(["foo","foobarooofoo", "foosplatofoo",]) == 'foo', commonsuffix(["foo","foobarooofoo", "foosplatofoo",]))

def suite():
    suite = unittest.makeSuite(Teststrutil, 'test')
    return suite


#!/usr/bin/env python
from Examples.fauxware import basic_symbolic_execution


def test():
    r = basic_symbolic_execution()
    assert b'SOSNEAKY' in r

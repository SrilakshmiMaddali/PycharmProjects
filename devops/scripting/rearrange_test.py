#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrane(unittest.TestCase):
    def test_basic(self):
        testcase = "Srilakshmi, Maddali"
        expected = "Maddali Srilakshmi"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Srilakshmi"
        expected = "Srilakshmi"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
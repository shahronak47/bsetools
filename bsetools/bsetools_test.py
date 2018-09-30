import unittest
from bsetools import bsetools

class TestBseTools(unittest.TestCase) :

    def test_types(self):
        self.assertRaises(TypeError, bsetools.get_quote, 23)
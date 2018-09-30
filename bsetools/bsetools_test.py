import unittest
from bsetools import bsetools

class TestBseTools(unittest.TestCase) :

    def test_types(self):
        #Test the various input types
        self.assertRaises(TypeError, bsetools.get_quote, 23)
        self.assertRaises(TypeError, bsetools.get_quote, True)

    def test_isinstance(self):
        #Test the output types
        obj = bsetools()
        quote, diff = obj.get_quote("Tech Mahindra")
        self.assertIsInstance(quote, str)

        self.assertIsInstance(diff, str)

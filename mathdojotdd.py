import unittest 
from mathdojo import *

class TestMathDojo(unittest.TestCase):

    def setUp(self):
        self.md = MathDojo()

    def test_add_subtract(self):
        self.assertEqual(self.md.add(2).add(2, 5, 1).subtract(3, 2).result, 5)

    def test_add(self):
        self.assertEqual(self.md.add(2).result, 2)



if __name__ == '__main__':
    unittest.main()
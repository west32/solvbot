import unittest
from min_max import maximum, minimum

class MinMaxTest(unittest.TestCase):

    def test_maximum(self):
        self.assertEqual(maximum([-52, 56, 30, 29, -54, 0, -110]), 56)
        self.assertEqual(maximum([4, 6, 2, 1, 9, 63, -134, 566]), 566)
        self.assertEqual(maximum([5]), 5)
        self.assertEqual(maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]), 555)
        self.assertEqual(maximum([9]), 9)

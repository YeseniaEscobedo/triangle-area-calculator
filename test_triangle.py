import unittest
from triangle import calculate_triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(calculate_triangle_area(10, 5), 25)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            calculate_triangle_area(-1, 5)

if __name__ == '__main__':
    unittest.main()

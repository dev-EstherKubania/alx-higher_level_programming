"""
    unittest for class square
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_instance(self):
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
    
    def test_negative_values_in_square(self):
        with self.assertRaises(ValueError):
            square = Square(-7)

    def test_x_and_y(self):
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(4, 2, 1, 12)
        s.display()

    def test_string_representation(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")
    
    def test_square_invalid_dimension(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_update(self):
        s = Square(1)
        s.update(2,4)
        self.assertEqual(s.__str__(), "[Square] (2) 0/0 - 4")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_invalid_x_and_y(self):
        with self.assertRaises(ValueError):
            s = Square(5, -2, 3)
        with self.assertRaises(ValueError):
            s = Square(5, 2, -3)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            s = Square("5")
        with self.assertRaises(TypeError):
            s = Square(5, "2", 3)

if __name__ == '__main__':
    unittest.main()


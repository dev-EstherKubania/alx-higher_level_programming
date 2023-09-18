"""
    unit test for class rectangle
"""
import json
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test class for the Rectangle class.
    """
    
    def test_rectangle_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_negative_values_in_rectangle(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_create_instance(self):
        r = Rectangle(5, 10)
        self.assertIsInstance(r, Rectangle)

    def test_attributes(self):
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_attributes_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2)

    def test_width_and_height(self):
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)

    def test_x_and_y(self):
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)

    def test_area_calculation(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display_method(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        import io
        from unittest.mock import patch
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    def test_string_representation(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1, 2)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")

if __name__ == '__main__':
    unittest.main()


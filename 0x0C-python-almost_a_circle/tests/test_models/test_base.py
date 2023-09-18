"""
    Test Case for class base.
"""
import unittest
from models.base import Base
from models.square import Square
import json


class TestBaseClass(unittest.TestCase):
    """
        Test class for the base class.
    """
    def test_create_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_non_empty_list(self):
        json_str = Base.to_json_string([{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}])
        self.assertEqual(json_str, '[{"id": 1, "name": "Object1"}, {"id": 2, "name": "Object2"}]')

    def test_from_json_string_empty_string(self):
        objects = Base.from_json_string("")
        self.assertEqual(objects, [])

    def test_from_json_string_non_empty_string(self):
        objects = Base.from_json_string('[{"id": 1, "name": "Object1"}, {"id": 2, "name": "Object2"}]')
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]['name'], 'Object1')
        self.assertEqual(objects[1]['name'], 'Object2')

    def test_id(self):
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_tuple(self):
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)

    def test_to_json_type(self):
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])

    def test_to_json_None(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_json_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        json_list = Base.from_json_string("[]")
        self.assertEqual(json_list, [])

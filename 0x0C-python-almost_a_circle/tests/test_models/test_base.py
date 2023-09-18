"""
    Test Case for class base.
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
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
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_idzero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_idnegative(self):
        b = Base(-3)
        self.assertEqual(-3, b.id)

    def test_idstring(self):
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_idlist(self):
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_idtuple(self):
        b = Base((1, 4))
        self.assertEqual((1, 4), b.id)

    def test_iddict(self):
        b = Base({'id': 10})
        self.assertEqual({'id': 10}, b.id)

    def test_json_type(self):
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_json_value(self):
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])

    def test_json_None(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_json_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_jsonstring(self):
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_jsonnone(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_jsonempty(self):
        json_list = Base.from_json_string("[]")
        self.assertEqual(json_list, [])
    
    def test_id_not_given(self):
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
    
    def test_private_attr_access(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)
    
    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        self.assertTrue(Base(100), self.__class__ == Base)
    
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_none_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (99) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_none_file(self):
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

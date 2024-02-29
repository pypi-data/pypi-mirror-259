import unittest
import datetime
from postlanganalytics.jsonutil import is_json_convertible


class TestClient(unittest.TestCase):
    def test_can_convert(self):
        objects = [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": "thirty"},
            "Just a string",
            12345,
            [1, 2, 3],
        ]
        for obj in objects:
            assert is_json_convertible(obj)

    def test_cannot_convert(self):
        objects = [{"name": "Doe", "dob": set([1990])}, {"name": "Alice", "dob": datetime.date(1990, 5, 17)}]
        for obj in objects:
            assert is_json_convertible(obj) is False

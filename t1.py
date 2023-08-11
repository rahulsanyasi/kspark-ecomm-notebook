import unittest
from main import add_new_notebook

class Test_add_new_notebook(unittest.TestCase):
    def test_add_new_notebook(self):
        actual = add_new_notebook({"id":105,"notebook_type":"Exercise Book","size":"20 x 26","pages":"180","type":"6 Subjects Note Book","price":180.0})
        expected = {"id":105,"notebook_type":"Exercise Book","size":"20 x 26","pages":"180","type":"6 Subjects Note Book","price":180.0}
        self.assertEqual(actual, expected)
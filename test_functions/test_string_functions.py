import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual("DerekDerekDerek", string_functions.multiply_string("Derek", 3))


if __name__ == '__main__':
    unittest.main()

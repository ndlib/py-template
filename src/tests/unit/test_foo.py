import unittest

from src import foo


class TestSum(unittest.TestCase):
    def test_add(self):
        result = foo.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()

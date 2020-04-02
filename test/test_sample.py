import unittest
from sample import add

class TestSample(unittest.TestCase):
    def test_success_sample(self):
        self.assertEqual(add(1, 2), 3, msg='function add is invalid')


if __name__ == '__main__':
    unittest.main()
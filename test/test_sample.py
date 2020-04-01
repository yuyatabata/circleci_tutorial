import unittest


class TestSample(unittest.TestCase):
    def test_success_sample(self):
        a = 1
        b = 1
        self.assertEqual(a, b, msg='a is not equals b')


if __name__ == '__main__':
    unittest.main()
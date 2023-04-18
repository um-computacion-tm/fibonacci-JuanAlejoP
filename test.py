import unittest
from fibonacci import fibonacci





class TestFibonacci(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, fibonacci(1))

if __name__ == '__main__':
    unittest.main()
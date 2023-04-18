import unittest
from fibonacci import fibonacci, fibonacci_1


class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci(1))

    def test_2(self):
        self.assertEqual(1, fibonacci(2))

    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))

    def test_5(self):
        self.assertEqual(5, fibonacci(5))

    def test_6(self):
        self.assertEqual(8, fibonacci(6))


if __name__ == '__main__':
    unittest.main()
import unittest

class TestMathOperations(unittest.TestCase):
    @staticmethod
    def test_addition():
        assert 1 + 1 == 2

    @staticmethod
    def test_subtraction():
        assert 2 - 1 == 1

if __name__ == "__main__":
    unittest.main()

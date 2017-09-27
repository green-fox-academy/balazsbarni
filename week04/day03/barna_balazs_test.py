import unittest
from barna_balazs_work import Apples

class Apples_test(unittest.TestCase):
    def test_get_apple(self):
        test_apple = Apples()
        self.assertEquals(test_apple.get_apple(), "apple")


if __name__ == '__main__':
    unittest.main()
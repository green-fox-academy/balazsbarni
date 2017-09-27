import unittest
from barna_balazs_work import My_Class
test_sum = My_Class()


class My_Class_Test(unittest.TestCase):
    def test_get_apple(self):
        test_apple = My_Class()
        self.assertEquals(test_apple.get_apple(), "apple")

    def test_get_sum_list_with_items(self):
        my_num = [2,3]
        self.assertEquals(test_sum.get_sum(my_num), 5)

    def test_get_sum_empty_list(self):
        empty_list = []
        self.assertEquals(test_sum.get_sum(empty_list), 0)

    def test_my_sum_one_element(self):
        one_item_list = [2]
        self.assertEquals(test_sum.get_sum(one_item_list), 2)

    def test_my_sum_multiple_element(self):
        multiple_item_list = [1, 2, 3, 4]
        self.assertEquals(test_sum.get_sum(multiple_item_list), 10)

    def test_my_sum_null(self):
        null_list = [0]
        self.assertEquals(test_sum.get_sum(null_list), 0)

if __name__ == '__main__':
    unittest.main()
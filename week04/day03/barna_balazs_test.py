import unittest
from barna_balazs_work import My_Class
test_sum = My_Class()
test_anagram = My_Class()


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


    def test_is_anagram_one_item(self):
        ana_one = "a"
        ana_two = "a"
        self.assertTrue(test_anagram.is_anagram(ana_one, ana_two))

    def test_is_anagram_empty(self):
        ana_one = ""
        ana_two = ""
        self.assertTrue(test_anagram.is_anagram(ana_one, ana_two))

    def test_is_anagram_not(self):
        ana_one = "a"
        ana_two = "b"
        self.assertFalse(test_anagram.is_anagram(ana_one, ana_two))

    def test_is_anagram_multiple_letters(self):
        ana_one = "abc"
        ana_two = "cba"
        self.assertTrue(test_anagram.is_anagram(ana_one, ana_two))

    def test_is_anagram_multiple_words(self):
        ana_one = "123 xyz"
        ana_two = "xyz 123"
        self.assertTrue(test_anagram.is_anagram(ana_one, ana_two))

if __name__ == '__main__':
    unittest.main()
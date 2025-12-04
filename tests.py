from main import *
import unittest


def valid_date(date):
    if (len(date) == 8) and (1900 <= int(date[:4]) <= 2025):
        if int(date[4:6]) in list(range(1, 8, 2)) + list(range(8, 13, 2)):
            return 1 <= int(date[6:]) <= 31
        elif 2 <= int(date[4:6]) <= 11:
            return 1 <= int(date[6:]) <= 30
    return False


def valid_code(code):
    return len(code) == 5 and all(i in '0123456789ABCDEF' for i in code)


class TestParser(unittest.TestCase):
    def test_nasa(self):
        self.assertTrue(valid_date(search_launch_voyager()))

    def test_rfc(self):
        self.assertTrue(valid_date(search_data_rfc()))

    def test_unicode(self):
        self.assertTrue(valid_code(search_brain_codepoint()))

    def test_bitcoin(self):
        self.assertTrue(valid_date(date_genesis_bitcoin_block()))

    def test_loc(self):
        self.assertTrue(len(search_book_isbn()) == 10)


if __name__ == '__main__':
    unittest.main()

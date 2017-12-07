import unittest


from adventofcode.day01.solution_part01 import inverse_captcha
from adventofcode.day01.solution_part02 import halfway_captcha


class TestDay01_Part1(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(inverse_captcha('1111'), 4)

    def test_sum2(self):
        self.assertEqual(inverse_captcha('1234'), 0)

    def test_sum3(self):
        self.assertEqual(inverse_captcha('1122'), 3)

    def test_sum4(self):
        self.assertEqual(inverse_captcha('91212129'), 9)

    def test_sum5(self):
        self.assertEqual(inverse_captcha('11011011'), 4)


class TestDay01_Part2(unittest.TestCase):

    def test_halfway1(self):
        self.assertEqual(halfway_captcha('1212'), 6)

    def test_halfway2(self):
        self.assertEqual(halfway_captcha('1221'), 0)

    def test_halfway3(self):
        self.assertEqual(halfway_captcha('123425'), 4)

    def test_halfway4(self):
        self.assertEqual(halfway_captcha('123123'), 12)

    def test_halfway5(self):
        self.assertEqual(halfway_captcha('12131415'), 4)


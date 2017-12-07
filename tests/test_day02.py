import unittest


from adventofcode.day02.solution_part01 import checksum
from adventofcode.day02.solution_part01 import checksum_line

from adventofcode.day02.solution_part02 import evenly_divisible
from adventofcode.day02.solution_part02 import sum_evenly_divided


class TestDay02_part1(unittest.TestCase):

    def test_checksum1(self):
        self.assertEqual(checksum_line([5, 1, 9, 5]), 8)

    def test_checksum2(self):
        self.assertEqual(checksum_line([7, 5, 3]), 4)

    def test_checksum3(self):
        self.assertEqual(checksum_line([2, 4, 6, 8]), 6)

    def test_checksum4(self):
        spreadsheet = [
            [5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]
        ]

        self.assertEqual(checksum(spreadsheet), 18)


class TestDay02_part2(unittest.TestCase):

    def test_evenly_divisible1(self):
        self.assertEqual(evenly_divisible([5, 9, 2, 8]), 4)

    def test_evenly_divisible2(self):
        self.assertEqual(evenly_divisible([9, 4, 7, 3]), 3)

    def test_evenly_divisible3(self):
        self.assertEqual(evenly_divisible([3, 8, 6, 5]), 2)

    def test_evenly_divisible4(self):
        spreadsheet = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]
        ]

        self.assertEqual(sum_evenly_divided(spreadsheet), 9)

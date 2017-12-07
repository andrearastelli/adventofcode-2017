import unittest


from adventofcode.day03.solution_part01 import manhattan_steps


class TestDay03_Part1(unittest.TestCase):

    def test_manhattan_steps1(self):
        self.assertEqual(manhattan_steps(1), 0)

    def test_manhattan_steps2(self):
        self.assertEqual(manhattan_steps(12), 3)

    def test_manhattan_steps3(self):
        self.assertEqual(manhattan_steps(23), 2)

    def test_manhattan_steps4(self):
        self.assertEqual(manhattan_steps(1024), 31)

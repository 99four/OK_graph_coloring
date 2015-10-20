from unittest import TestCase
from bruteforce import Bruteforce
__author__ = 'Damian'


class TestBruteforce(TestCase):
    def test_first_is_zeros(self):
        b = Bruteforce(digits=3, bound=2)

        expected = [0, 0, 0]
        actual = b.first()

        self.assertListEqual(expected, actual)

    def test_increment_zero(self):
        b = Bruteforce(digits=4, bound=4)

        expected = [0, 0, 0 ,1]
        actual = b.increment([0,0,0,0])

        self.assertListEqual(expected, actual)

    def test_increment_with_carry(self):
        b = Bruteforce(digits=4, bound=4)

        expected = [0, 0, 1 ,0]
        actual = b.increment([0,0,0,3])

        self.assertListEqual(expected, actual)

    def test_overflow(self):
        b = Bruteforce(digits=5, bound=7)

        self.assertRaises(Exception, b.increment, [6,6,6,6,6])

    def test_range(self):
        b = Bruteforce(digits=2, bound=3)

        expected = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        actual = b.range()

        self.assertListEqual(expected, actual)






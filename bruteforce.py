#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Damian'

class Bruteforce:
    def __init__(self, digits, bound):
        self.digits = digits
        self.bound = bound

    def first(self):
        return [0] * self.digits

    def increment(self, num, pos=-1):
        assert len(num) == self.digits

        if num == [self.bound-1] * self.digits:
            raise Exception('Wyszedlem poza tablice')

        following = num[:]
        following[pos] += 1

        if following[pos] >= self.bound:
            following[pos] = 0
            return self.increment(following, pos - 1)

        return following

    def range(self):
        numbers = [self.first()]
        for d in range(1,self.bound**self.digits):
            numbers.append(self.increment(numbers[-1]))
        return numbers


if __name__ == "__main__":
    print("asdf")
    b = Bruteforce(digits=5,bound=6)
    #print(b.increment(b.first()))
    print (b.range())
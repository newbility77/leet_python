"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
import unittest
import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        assert(isinstance(x, int))
        assert(x >= 0)
        if x == 0:
            return 0
        elif x < 4:
            return 1
        s = 2
        e = x // 2
        while s + 1 < e:
            m = (s + e) // 2
            m2 = m ** 2
            if m2 == x:
                return m
            elif m2 < x:
                s = m
            else:
                e = m
        return s


class TestSolution(unittest.TestCase):
    def test_my_sqrt(self):
        sol = Solution()
        # print(sol.mySqrt(12))
        for x in range(1000):
            self.assertEqual(sol.mySqrt(x), int(math.sqrt(x)), x)

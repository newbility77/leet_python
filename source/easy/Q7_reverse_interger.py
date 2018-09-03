"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import unittest

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xc = abs(x)
        rev = 0
        while xc != 0:
            rev = rev * 10 + xc % 10
            xc = xc // 10
        rev = -rev if x < 0 else rev
        return 0 if rev < -2**31 or rev > 2**31 - 1 else rev


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer(self):
        sol = Solution()
        self.assertEqual(-321, sol.reverse(-123))
        self.assertEqual(21, sol.reverse(120))
        self.assertEqual(0, sol.reverse(1999999999))

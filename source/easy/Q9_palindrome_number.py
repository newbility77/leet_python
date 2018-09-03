"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            if rev == x:
                return True
            x = x // 10

        return x == rev


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome(121))
        self.assertFalse(sol.isPalindrome(-121))
        self.assertFalse(sol.isPalindrome(10))
        self.assertTrue(sol.isPalindrome(0))
        self.assertTrue(sol.isPalindrome(1))
        self.assertFalse(sol.isPalindrome(21120))

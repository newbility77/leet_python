"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
import unittest


class Solution:
    def longest_palindrome_brute_force(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for start in range(len(s)):
            for end in range(start + len(longest) + 1, len(s)):
                if self.is_palindrome(s[start:end]):
                    longest = s[start:end]
        return longest

    def is_palindrome(self, s):
        for ii in range(len(s) // 2):
            if s[ii] != s[len(s) - ii - 1]:
                return False
        return True

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for start in range(len(s)):
            for end in range(start + len(longest) + 1, len(s)):
                ()


class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        sol = Solution()
        self.assertEqual("",    sol.longest_palindrome_brute_force(""))
        self.assertEqual("bab", sol.longest_palindrome_brute_force("babad"))
        self.assertEqual("bb",  sol.longest_palindrome_brute_force("cbbd"))

        self.assertEqual("",    sol.longest_palindrome(""))
        self.assertEqual("bab", sol.longest_palindrome("babad"))
        self.assertEqual("bb",  sol.longest_palindrome("cbbd"))

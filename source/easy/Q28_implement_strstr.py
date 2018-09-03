"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        left, right = 0, len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1


class TestSolution(unittest.TestCase):
    def test_strstr(self):
        sol = Solution()
        self.assertEqual(2, sol.strStr("hello", "ll"))
        self.assertEqual(-1, sol.strStr("aaaaa", "bba"))
        self.assertEqual(0, sol.strStr("abc", ""))
        self.assertEqual(0, sol.strStr("a", "a"))

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
import unittest


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {"{": "}",
               "[": "]",
               "(": ")"}
        for ps in s:
            if ps in pair:
                stack.append(pair[ps])
            elif len(stack) == 0:
                return False
            elif stack.pop() != ps:
                return False
        return len(stack) == 0


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        sol = Solution()
        self.assertTrue(sol.isValid("()"))
        self.assertTrue(sol.isValid("()[]{}"))
        self.assertFalse(sol.isValid("(]"))
        self.assertFalse(sol.isValid("([)]"))
        self.assertTrue(sol.isValid("{[]}"))
        self.assertTrue(sol.isValid(""))
        self.assertFalse(sol.isValid("}"))
        self.assertFalse(sol.isValid("["))
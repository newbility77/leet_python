"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
import unittest


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = s.rstrip()
        if st:
            st = " " + st
            ind = st.rfind(" ")
            return len(st) - 1 - ind
        else:
            return 0

class TestSolution(unittest.TestCase):
    def test_length_of_last_word(self):
        sol = Solution()
        self.assertEqual(0, sol.lengthOfLastWord(""))
        self.assertEqual(0, sol.lengthOfLastWord(" "))
        self.assertEqual(3, sol.lengthOfLastWord("abc"))
        self.assertEqual(3, sol.lengthOfLastWord("abc "))
        self.assertEqual(3, sol.lengthOfLastWord(" abc"))
        self.assertEqual(3, sol.lengthOfLastWord(" abc "))
        self.assertEqual(4, sol.lengthOfLastWord("abc defg"))
        self.assertEqual(4, sol.lengthOfLastWord("abc defg  "))
        self.assertEqual(5, sol.lengthOfLastWord("Hello World"))

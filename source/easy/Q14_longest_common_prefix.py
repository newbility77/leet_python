"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
import unittest


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        for ii in range(len(strs[0])):
            next_c = strs[0][ii]
            for jj in range(len(strs) - 1):
                c = next_c
                next_c = "" if ii >= len(strs[jj + 1]) else strs[jj + 1][ii]
                if c != next_c:
                    return strs[0][:ii]
        return strs[0]


class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        sol = Solution()
        self.assertEqual("fl", sol.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual("", sol.longestCommonPrefix(["dog", "racecar", "car"]))
        self.assertEqual("a", sol.longestCommonPrefix(["aa", "a"]))
        self.assertEqual("aa", sol.longestCommonPrefix(["aa"]))

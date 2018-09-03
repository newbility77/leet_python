"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the ansnwer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
import unittest


class Solution:
    def longest_substring_without_repeating_characters(self, str):
        """
        :type s: str
        :rtype: int
        """
        if str is None or len(str) == 0:
            return 0
        start, end = 0, 0
        exist_dict = {}
        current_start = 0
        for index, elem in enumerate(str):
            if elem in exist_dict and current_start <= exist_dict[elem]:
                current_start = exist_dict[elem] + 1
            exist_dict[elem] = index
            if index - current_start > end - start:
                start = current_start
                end = index
            # print(start, end, str[start:end + 1], current_start, index, str[current_start:index + 1])
            # print(exist_dict)
        return end - start + 1


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_longest_substring_without_repeating_characters(self):
        sol = Solution()
        self.assertEqual(3, sol.longest_substring_without_repeating_characters("abcabcbb"))
        self.assertEqual(1, sol.longest_substring_without_repeating_characters("bbbbb"))
        self.assertEqual(3, sol.longest_substring_without_repeating_characters("pwwkew"))
        self.assertEqual(0, sol.longest_substring_without_repeating_characters(""))

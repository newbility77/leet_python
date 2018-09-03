"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest


class Solution(object):
    def two_sum(self, nums, target):
        element_dict = {}
        for index, element in enumerate(nums):
            if element in element_dict:
                return [element_dict[element], index]
            element_dict[target - element] = index
        return None


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        sol = Solution()
        self.assertEqual([0, 1], sol.two_sum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], sol.two_sum([15, 7, 2, 11], 9))

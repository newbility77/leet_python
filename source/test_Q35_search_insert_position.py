"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
import unittest


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        s, e = 0, len(nums) - 1
        while s + 1 < e:
            m = (s + e) // 2
            nm = nums[m]
            if nm == target:
                return m
            elif nm < target:
                s = m + 1
            else:
                e = m - 1
        if nums[s] == target:
            return s
        if nums[e] == target:
            return e
        return s + 1


class TestSolution(unittest.TestCase):
    def test_search_insert(self):
        sol = Solution()
        self.assertEqual(2, sol.searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, sol.searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, sol.searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, sol.searchInsert([1, 3, 5, 6], 0))

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
import unittest


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        cur_sum = 0
        for ii in nums:
            if cur_sum < 0:
                cur_sum = ii
            else:
                cur_sum += ii
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


class TestSolution(unittest.TestCase):
    def test_max_sub_array(self):
        sol = Solution()
        self.assertEqual(6, sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(0, sol.maxSubArray([]))
        self.assertEqual(1, sol.maxSubArray([1]))
        self.assertEqual(-1, sol.maxSubArray([-1]))

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
import unittest


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m1, n1, k = m - 1, n - 1, m + n - 1
        while m1 >= 0 and n1 >= 0:
            if nums1[m1] >= nums2[n1]:
                nums1[k], m1 = nums1[m1], m1 - 1
            else:
                nums1[k], n1 = nums2[n1], n1 - 1
            k -= 1
        if n1 >= 0:
            nums1[:n1 + 1] = nums2[:n1 + 1]


class TestSolution(unittest.TestCase):
    def test_delete_duplicates(self):
        sol = Solution()
        n1 = [1, 2, 3, 0, 0, 0]
        n2 = [2, 5, 6]
        sol.merge(n1, 3, n2, 3)
        self.assertEqual([1, 2, 2, 3, 5, 6], n1)

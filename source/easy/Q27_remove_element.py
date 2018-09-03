"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
import unittest


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        first = 0
        last = len(nums) - 1
        while first <= last:
            while first <= last and nums[last] == val:
                last -= 1
            while first <= last and nums[first] != val:
                first += 1
            if first < last:
                nums[first] = nums[last]
                last -= 1
                first += 1
        return first


class TestSolution(unittest.TestCase):
    def test_remove_element(self):
        sol = Solution()
        nums = [3, 2, 2, 3]
        self.assertEqual(sol.removeElement(nums, 3), 2)
        self.assertEqual(sorted(nums[:2]), sorted([2, 2]))

        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        self.assertEqual(sol.removeElement(nums, 2), 5)
        self.assertEqual(sorted(nums[:5]), sorted([0, 1, 3, 0, 4]))

        self.assertEqual(sol.removeElement([0, 0, 0], 0), 0)

        nums = [0, 0, 1]
        self.assertEqual(sol.removeElement(nums, 0), 1)
        self.assertEqual(sorted(nums[:1]), [1])

        nums = [0, 1, 1]
        self.assertEqual(sol.removeElement(nums, 1), 1)
        self.assertEqual(sorted(nums[:1]), [0])

        nums = []
        self.assertEqual(sol.removeElement(nums, 1), 0)
        self.assertEqual(sorted(nums), [])

        nums = None
        self.assertEqual(sol.removeElement(nums, 1), 0)

        nums = [4, 5]
        self.assertEqual(sol.removeElement(nums, 4), 1)
        self.assertEqual(sorted(nums[:1]), [5])

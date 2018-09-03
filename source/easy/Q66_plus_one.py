"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
import unittest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        for ii in range(-1, -len(digits) - 1, -1):
            if digits[ii] < 9:
                digits[ii] = digits[ii] + 1
                break
            else:
                digits[ii] = 0
        return digits if digits[0] == 1 else digits[1:]


class TestSolution(unittest.TestCase):
    def test_plus_one(self):
        sol = Solution()
        self.assertEqual([1, 2, 4], sol.plusOne([1, 2, 3]))
        self.assertEqual([4, 3, 2, 2], sol.plusOne([4, 3, 2, 1]))
        self.assertEqual([1, 0], sol.plusOne([9]))
        self.assertEqual([1, 0, 0], sol.plusOne([9, 9]))
        self.assertEqual([9, 0, 0], sol.plusOne([8, 9, 9]))
        self.assertEqual([9,8,7,6,5,4,3,2,1,1], sol.plusOne([9,8,7,6,5,4,3,2,1,0]))
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def is_balanced(cls, root):
        if not root:
            return True, 0
        else:
            left = TreeNode.is_balanced(root.left)
            right = TreeNode.is_balanced(root.right)
            return left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None
            mid = (right + left) >> 1
            root, root.left, root.right = TreeNode(nums[mid]), helper(left, mid - 1), helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

class TestSolution(unittest.TestCase):
    def test_sorted_array_to_bst(self):
        sol = Solution()
        arr = [-10, -3, 0, 5, 9]
        self.assertTrue(TreeNode.is_balanced(sol.sortedArrayToBST(arr)))

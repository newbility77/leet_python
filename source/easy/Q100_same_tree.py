"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return not p and not q


class TestSolution(unittest.TestCase):
    def test_is_same_tree(self):
        sol = Solution()
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertTrue(sol.isSameTree(root1, root2))
        root1 = TreeNode(0)
        root1.left = TreeNode(-5)
        root2 = TreeNode(0)
        root2.left = TreeNode(-8)
        self.assertFalse(sol.isSameTree(root1, root2))

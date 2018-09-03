"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        if root.left:
            depth = self.minDepth(root.left)
        if root.right:
            depth = min(self.minDepth(root.right), depth) if root.left else self.minDepth(root.right)
        return depth + 1


class TestSolution(unittest.TestCase):
    def test_sorted_array_to_bst(self):
        sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(2, sol.minDepth(root))

        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(2, sol.minDepth(root))

        root = None
        self.assertEqual(0, sol.minDepth(root))

        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(2, sol.minDepth(root))


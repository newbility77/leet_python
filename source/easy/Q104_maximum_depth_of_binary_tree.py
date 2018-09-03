"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepthRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right)) + 1 if root else 0

    def maxDepthStack(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 1
        stack = [(1, root)]
        while stack:
            node = stack.pop()
            if node[1].left or node[1].right:
                depth = node[0] + 1
                max_depth = max(max_depth, depth)
                if node[1].left:
                    stack.append((depth, node[1].left))
                if node[1].right:
                    stack.append((depth, node[1].right))
        return max_depth

class TestSolution(unittest.TestCase):
    def test_max_depth(self):
        sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(3, sol.maxDepthRecursive(root))
        self.assertEqual(3, sol.maxDepthStack(root))

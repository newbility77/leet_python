"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left and right:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return not left and not right


class TestSolution(unittest.TestCase):
    def test_is_same_tree(self):
        sol = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(sol.isSymmetric(root))

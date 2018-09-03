"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        current = [root]
        result = []
        while current:
            local_result = []
            next_level = []
            for elem in current:
                if not elem:
                    continue
                local_result.append(elem.val)
                next_level.append(elem.left)
                next_level.append(elem.right)
            current = next_level
            result.insert(0, local_result)
        return result if result[0] else result[1:]


class TestSolution(unittest.TestCase):
    def test_level_order_bottom(self):
        sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual([[15, 7], [9, 20], [3]], sol.levelOrderBottom(root))
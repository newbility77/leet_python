"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        n = head
        while n.next:
            if n.next.val == n.val:
                n.next = n.next.next
            else:
                n = n.next
        return head


class TestSolution(unittest.TestCase):
    def test_delete_duplicates(self):
        sol = Solution()
        # 1->1->2
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head = sol.deleteDuplicates(head)
        self.assertEqual(head.val, 1)
        self.assertTrue(head.next)
        self.assertEqual(head.next.val, 2)
        self.assertFalse(head.next.next)

        # 1->1->2->3->3
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        head = sol.deleteDuplicates(head)
        self.assertEqual(head.val, 1)
        self.assertTrue(head.next)
        self.assertEqual(head.next.val, 2)
        self.assertTrue(head.next.next)
        self.assertEqual(head.next.next.val, 3)
        self.assertFalse(head.next.next.next)

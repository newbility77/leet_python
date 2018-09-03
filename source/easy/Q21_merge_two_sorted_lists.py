"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        if self.val != other.val:
            return False
        if self.next is None and other.next is None:
            return True
        if self.next is None or other.next is None:
            return False
        return self.next.__eq__(other.next)


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1)
        l3c = l3
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l3c.next = l1
                l1 = l1.next
            else:
                l3c.next = l2
                l2 = l2.next
            l3c = l3c.next

        l3c.next = l1 or l2
        return l3.next


class TestMergeTwoLists(unittest.TestCase):
    def test_merge_two_lists(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        l3 = ListNode(1)
        l3.next = ListNode(1)
        l3.next.next = ListNode(2)
        l3.next.next.next = ListNode(3)
        l3.next.next.next.next = ListNode(4)
        l3.next.next.next.next.next = ListNode(4)
        sol = Solution()
        self.assertEqual(sol.mergeTwoLists(l1, l2), l3)
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(1)
        l3.next = ListNode(2)
        self.assertEqual(sol.mergeTwoLists(l1, l2), l3)

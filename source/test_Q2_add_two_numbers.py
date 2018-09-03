"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        result = str(self.val)
        if self.next is not None:
            result += "=>"
            result += self.next.__repr__()
        return result


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        l = None
        n = None
        carry = 0
        while n1 is not None or n2 is not None:
            n1v, n1 = (n1.val, n1.next) if n1 is not None else (0, None)
            n2v, n2 = (n2.val, n2.next) if n2 is not None else (0, None)
            carry = n1v + n2v + carry
            m = ListNode(carry % 10)
            carry = carry // 10
            if l is None:
                l = m
            else:
                n.next = m
            n = m
        if carry != 0:
            m = ListNode(carry)
            n.next = m
        return l


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        sol = Solution()
        l1 = ListNode(0)
        l2 = ListNode(0)
        res = ListNode(0)
        self.assertEqual(res, sol.addTwoNumbers(l1, l2))
        l1 = ListNode(5)
        l2 = ListNode(5)
        res = ListNode(0)
        res.next = ListNode(1)
        self.assertEqual(res, sol.addTwoNumbers(l1, l2))

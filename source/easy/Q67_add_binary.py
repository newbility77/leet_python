"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_len, b_len = len(a), len(b)
        m_len = max(a_len, b_len) + 1
        a, b = "0"*(m_len - a_len) + a, "0"*(m_len - b_len) + b
        carry, c = 0, []
        for tup in zip(a[::-1], b[::-1]):
            n = int(tup[0]) + int(tup[1]) + carry
            carry, cn = divmod(n, 2)
            c.append(str(cn))
        return "".join(c[-2::-1] if c[-1] == "0" else c[::-1])


class TestSolution(unittest.TestCase):
    def test_add_binary(self):
        sol = Solution()
        self.assertEqual("100", sol.addBinary("11", "1"))
        self.assertEqual("10101", sol.addBinary("1010", "1011"))
        self.assertEqual("0", sol.addBinary("0", "0"))

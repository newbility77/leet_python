"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
import unittest


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_1 = "1"
        if n == 1:
            return n_1
        for i in range(1, n):
            ss = []
            last = [0, n_1[0]]
            for c in n_1:
                if last[1] == c:
                    last[0] += 1
                else:
                    ss.append(last)
                    last = [1, c]
            ss.append(last)
            n_1 = "".join([str(s[0]) + s[1] for s in ss])
        return n_1

class TestSolution(unittest.TestCase):
    def test_count_and_say(self):
        sol = Solution()
        self.assertEqual("1", sol.countAndSay(1))
        self.assertEqual("11", sol.countAndSay(2))
        self.assertEqual("21", sol.countAndSay(3))
        self.assertEqual("1211", sol.countAndSay(4))
        self.assertEqual("111221", sol.countAndSay(5))

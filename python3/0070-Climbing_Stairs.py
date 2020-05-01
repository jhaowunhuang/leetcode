class Solution:
    def climbStairs(self, n):
        pre1, pre2 = 0, 1
        while n > 0:
            pre1, pre2 = pre2, pre1 + pre2
            n -= 1
        return pre2

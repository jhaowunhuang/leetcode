class Solution:
    def climbStairs(self, n):
        pre, cur = 0, 1
        while n > 0:
            pre, cur = cur, pre + cur
            n -= 1
        return cur 

class Solution:
    def reverse(self, x):
        sign = 0
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        ans = 0
        while x:
            ans = x % 10 + ans * 10
            x //= 10
        ans *= sign
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        return ans

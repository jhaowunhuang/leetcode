class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x // 2 + 1
        mid = (left + right) // 2
        while mid - left >= 1:
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                right = mid
            else:
                left = mid
            mid = (left + right) // 2
        return mid

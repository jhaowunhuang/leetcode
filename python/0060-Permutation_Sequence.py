import math
class Solution:
    def getPermutation(self, n, k):
        ref = [str(x) for x in range(1, n + 1)]
        fac = math.factorial(n)
        ans = ''
        for i in range(n, 0, -1):
            fac //= i
            r, k = divmod(k, fac)
            ans += ref.pop(r if k != 0 else r - 1)
        return ans

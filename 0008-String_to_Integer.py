class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ans = ''
        for i in s:
            if i.isdigit():
                ans += i
            else:
                if ans:
                    break
                if not sign:
                    if i == ' ':
                        continue
                    elif i == '+' or i == '-':
                        sign = i
                        continue
                return 0
        if not ans:
            return 0
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        ans = int(sign + ans)
        if ans > max_int:
            return max_int
        if ans < min_int:
            return min_int
        return ans

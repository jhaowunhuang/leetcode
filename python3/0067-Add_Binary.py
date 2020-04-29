class Solution:
    def addBinary(self, a, b):
        ans = ''
        a = list(a)
        b = list(b)
        r = 0
        while a or b or r:
            if a:
                r += int(a.pop())
            if b:
                r += int(b.pop())
            r, d = divmod(r, 2)
            ans = str(d) + ans
        return ans

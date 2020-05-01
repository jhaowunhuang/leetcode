class Solution:
    def plusOne(self, digits):
        r = 1
        i = len(digits) - 1
        while r and i >= 0:
            r, digits[i] = divmod(r + digits[i], 10)
            i -= 1
        if r:
            digits.insert(0, r)
        return digits

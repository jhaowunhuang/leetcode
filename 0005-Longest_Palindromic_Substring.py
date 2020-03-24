class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2 or s == s[::-1]:
            return s
        start, max_len = 0, 1
        for i in range(1, s_len):
            odd_start = i - max_len - 1
            even_start = i - max_len
            odd = s[odd_start:i + 1]
            even = s[even_start:i + 1]
            if odd_start >= 0 and odd == odd[::-1]:
                start = odd_start
                max_len += 2
            elif even_start >= 0 and even == even[::-1]:
                start = even_start
                max_len += 1
        return s[start:start + max_len]

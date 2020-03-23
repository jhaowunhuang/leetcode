class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = {}
        ans = i = 0
        for j, item in enumerate(s):
            if item in ref:
                i = max(i, ref[item] + 1)
            ans = max(ans, j - i + 1)
            ref[item] = j
        return ans

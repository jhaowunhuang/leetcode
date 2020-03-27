class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:  return ''
        ans = strs[0]
        for s in strs[1:]:
            for j in range(len(ans), -1, -1):
                if ans == s[:j]:
                    break
                ans = ans[:-1]
        return ans

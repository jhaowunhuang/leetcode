class Solution:
    def getRow(self, rowInde):
        ans = [1]
        for i in range(1, rowIndex + 1):
            ans = [1] + [ans[j] + ans[j + 1] for j in range(i - 1)] + [1]
        return ans

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(numRows - 1):
            ans.append([1] + [ans[i][j] + ans[i][j + 1] for j in range(i)] + [1])
        return ans

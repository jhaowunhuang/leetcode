class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        ans = [''] * numRows
        row, move = 0, 1
        for i in s:
            if row == 0:
                move = 1
            elif row == numRows - 1:
                move = -1
            ans[row] += i
            row += move
        return ''.join(ans)

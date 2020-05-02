class Solution:
    def combine(self, n, k):
        ans = []
        n += 1
        def func(pos, temp, res):
            if res == 0:
                ans.append(temp)
            else:
                for i in range(pos, n - res + 1):
                    func(i + 1, temp + [i], res - 1)
        func(1, [], k)
        return ans

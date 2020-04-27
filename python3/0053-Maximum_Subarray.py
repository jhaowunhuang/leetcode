class Solution:
    def maxSubArray(self, nums):
        dp_arr = [0] * len(nums)
        dp_arr[0] = nums[0]
        for i, item in enumerate(nums):
            if i:
                dp_arr[i] = max(dp_arr[i - 1] + item, item)
        return max(dp_arr)

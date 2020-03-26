class Solution:
    def twoSum(nums, target):
        ref = {}
        for i, item in enumerate(nums):
            if target - item in ref:
                return [ref[target - item], i]
            ref[item] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i, item in enumerate(nums):
            if target - item in ref:
                return [ref[target - item], i]
            ref[item] = i

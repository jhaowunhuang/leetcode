class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, item in enumerate(nums):
            if item >= target:
                return i
        return len(nums)

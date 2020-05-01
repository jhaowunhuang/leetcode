import bisect


class Solution:
    def threeSum(self, nums):
        ref = {}
        for i in nums:
            ref[i] = ref.get(i, 0) + 1
        nums = sorted(ref)
        ans = []
        for i, item_i in enumerate(nums):
            if item_i == 0:
                if ref[item_i] > 2:
                    ans.append((0, 0, 0))
            else:
                if ref[item_i] > 1 and -2 * item_i in ref:
                    ans.append((item_i, item_i, -2 * item_i))
            if item_i < 0:
                target = -item_i
                left = bisect.bisect_left(nums, target - nums[-1], i + 1)
                right = bisect.bisect_right(nums, target // 2, left)
                for item_j in nums[left:right]:
                    item_k = target - item_j
                    if item_k in ref and item_k != item_j:
                        ans.append((item_i, item_j, item_k))
        return ans

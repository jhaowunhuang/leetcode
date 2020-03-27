class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_ans = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] > height[right]:
                max_ans = max(max_ans, (right - left) * height[right])
                right -= 1
            else:
                max_ans = max(max_ans, (right - left) * height[left])
                left += 1
        return max_ans

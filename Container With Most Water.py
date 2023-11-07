class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(height)-1

        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_vol = max(area, max_vol)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return max_vol


"""
Time - O(N)
Space - O(1)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            cap = (right - left)*min(heights[right],heights[left])
            if cap > mx:
                mx = cap 
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mx
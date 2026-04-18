class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxCapacity = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            capacity = height * width

            if capacity > maxCapacity:
                maxCapacity = capacity
        
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxCapacity
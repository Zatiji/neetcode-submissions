class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxRight = height[right]
        maxLeft = height[left]
        totalCapacity = 0

        while left < right:

            if maxRight < maxLeft:
                right -= 1
                capacity = maxRight - height[right]

                if capacity > 0:
                    totalCapacity += capacity
                
                maxRight = max(maxRight, height[right])
            
            else:
                left += 1
                capacity = maxLeft - height[left]

                if capacity > 0:
                    totalCapacity += capacity

                maxLeft = max(maxLeft, height[left])
        
        return totalCapacity




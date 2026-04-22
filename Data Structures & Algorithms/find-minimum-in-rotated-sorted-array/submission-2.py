class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        value = nums[0]

        while l <= r:
            m = l + ((r - l) // 2)
            left, right, mid = nums[l], nums[r], nums[m]

            if left > mid:
                r = m - 1
            elif right < mid:
                l = m + 1
            else:
                r = m - 1
            
            value = min(value, mid)
        
        return value

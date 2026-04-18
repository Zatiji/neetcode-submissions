class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = 0
        left = 0

        while right < len(nums) and left < len(nums):
            if nums[left] == val:
                while right < len(nums) and nums[right] == val:
                    right += 1
                
                if right < len(nums):
                    nums[left] = nums[right]
                    nums[right] = val
                    left += 1
            else:
                left += 1
                right += 1

        return left
            
        
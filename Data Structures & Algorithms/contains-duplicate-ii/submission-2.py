class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        left = 0
        right = 0
        while right < len(nums):
            
            if nums[left] == nums[right] and left != right:
                return True 

            else:
                right += 1
                if right - left > k and right < len(nums):
                    while left != right:
                        left += 1
                        if nums[left] == nums[right] and left != right:
                            return True
        
        return False


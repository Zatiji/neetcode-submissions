class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return len(nums)
        
        i = 1
        while i < size:
            if nums[i-1] == nums[i]:
                del nums[i]
                size -= 1
            else:
                i += 1

        return size
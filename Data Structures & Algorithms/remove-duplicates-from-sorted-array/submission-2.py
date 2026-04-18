class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size

        left = 1
        right = 1
        while right < size:
            if nums[right] > nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left




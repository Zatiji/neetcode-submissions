class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixes = []

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefixes.append(prefix)
        
        for i in range(len(nums)):
            sumLeft = prefixes[i] - nums[i]
            sumRight = prefixes[len(nums)-1] - prefixes[i]

            if sumLeft == sumRight:
                return i
        
        return -1
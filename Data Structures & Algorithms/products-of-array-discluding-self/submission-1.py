class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffixe = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffixe
            suffixe *= nums[i]
        
        return ans




        
        
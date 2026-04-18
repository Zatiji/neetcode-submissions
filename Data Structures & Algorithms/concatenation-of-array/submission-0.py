class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, 2*len(nums)):
            index = i % len(nums)
            ans.append(nums[index])
        
        return ans

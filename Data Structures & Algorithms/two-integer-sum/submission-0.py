class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            searchedValue = target - nums[i]

            if searchedValue in seen:
                return [seen[searchedValue], i]

            seen[nums[i]] = i
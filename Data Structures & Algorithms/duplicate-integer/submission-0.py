from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)

        for n in nums:
            if hashmap[n] > 1:
                return True
            
        return False
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixHash =  {0: 1}

        prefix = 0
        result = 0

        for n in nums:
            prefix += n
            subtractResult = prefix - k

            if subtractResult in prefixHash:
                result += prefixHash[subtractResult]
            
            prefixHash[prefix] = 1 + prefixHash.get(prefix, 0)
        
        return result
            
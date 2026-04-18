from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums) + 1)]
        count = {}    

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            frequency[count].append(num)
        
        response = []

        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                response.append(num)

                if len(response) == k:
                    return response




        

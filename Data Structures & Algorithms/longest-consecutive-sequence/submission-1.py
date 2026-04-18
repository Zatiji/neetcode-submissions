class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        answer = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:

                num = nums[i]
                sequenceLenght = 0

                while num in numSet:
                    sequenceLenght += 1
                    num += 1
                
                answer = max(sequenceLenght, answer)
        
        return answer
            
        

        

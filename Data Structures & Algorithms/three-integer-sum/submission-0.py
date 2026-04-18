class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            
            b = a + 1
            c = len(nums) - 1
            while b < c:
                result = nums[a] + nums[b] + nums[c] 
                if result > 0:
                    c -= 1
                elif result < 0:
                    b += 1
                else:
                    answers.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b] == nums[b-1] and b < c:
                        b += 1
        
        return answers

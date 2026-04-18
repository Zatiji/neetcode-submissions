class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixe = [1] * n
        for i in range(1, n):
            prefixe[i] = prefixe[i-1] * nums[i-1]

        suffixe = [1] * n
        i = n - 2
        while i >= 0:
            suffixe[i] = suffixe[i+1] * nums[i+1]
            i -= 1

        answer = []
        for i in range(n):
            result = prefixe[i] * suffixe[i]
            answer.append(result)
        
        return answer
            



        
        
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumSubArray = 0
        numSubArrays = 0
        
        right = 0
        left = 0
        while right < len(arr):

            sumSubArray += arr[right]

            if right - left >= k:
                sumSubArray -= arr[left]
                left += 1

            if sumSubArray >= threshold*k and right - left == k - 1:
                numSubArrays += 1
            
            right += 1
        
        return numSubArrays
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            
            result = numbers[left] + numbers[right]
            if result > target:
                right -= 1
            elif result < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]
            
            

            
        

        
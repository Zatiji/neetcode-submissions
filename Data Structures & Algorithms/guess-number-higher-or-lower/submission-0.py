# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_value, max_value = 1, n

        while min_value <= max_value:
            middle_value = min_value + (max_value - min_value) // 2

            result = guess(middle_value)

            if result > 0:
                min_value = middle_value + 1
            elif result < 0:
                max_value = middle_value - 1
            else:
                return middle_value
        
        return middle_value
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = [c for c in s if (c.isalpha() or c.isdigit())]
        trimmed = (''.join(sList)).lower()

        left = 0
        right = len(trimmed) - 1

        while left < right:
            if trimmed[left] != trimmed[right]:
                print(trimmed[left])
                print(trimmed[right])
                return False
            
            left += 1
            right -= 1
        
        return True
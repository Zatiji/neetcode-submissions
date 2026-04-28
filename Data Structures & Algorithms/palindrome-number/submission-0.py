class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1
        
        return True
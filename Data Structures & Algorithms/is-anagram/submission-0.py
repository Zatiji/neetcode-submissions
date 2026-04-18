from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = Counter(s)
        hashMapT = Counter(t)

        keyS = list(hashMapS.keys())
        keyT = list(hashMapT.keys())

        for key in keyS:
            if key not in hashMapT:
                return False
            if hashMapS[key] != hashMapT[key]:
                return False
        
        for key in keyT:
            if key not in hashMapS:
                return False
        
        return True
        
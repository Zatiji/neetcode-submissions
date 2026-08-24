# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2
        left = self.mergeSort(pairs[:m])
        right = self.mergeSort(pairs[m:])
        
        l = 0
        r = 0
        p = 0
        while p < len(pairs):
            if l >= len(left):
                pairs[p] = right[r]
                r += 1
            elif r >= len(right):
                pairs[p] = left[l]
                l += 1
            else:
                if left[l].key <= right[r].key:
                    pairs[p] = left[l]
                    l += 1
                else:
                    pairs[p] = right[r]
                    r += 1
            p += 1
        
        return pairs

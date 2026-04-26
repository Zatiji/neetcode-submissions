class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = 0
        s = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        p1 = s
        p2 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[p2]
            if p1 == p2:
                break
        
        return p1
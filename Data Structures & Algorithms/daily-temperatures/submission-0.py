class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # [index, value]

        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][1]:
                valueTuple = stack.pop()
                index = valueTuple[0]
                ans[index] = i - index
            
            stack.append([i, temperatures[i]])
        
        return ans


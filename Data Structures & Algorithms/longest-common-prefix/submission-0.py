class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        min_lenght = 201
        for s in strs:
            min_lenght = min(min_lenght, len(s))
        
        for i in range(min_lenght):
            for j in range(len(strs)):
                letter = strs[j][i]

                if j != 0:
                    if letter != strs[j - 1][i]:
                        return ''.join(prefix)
                
            prefix.append(strs[0][i])
        
        return ''.join(prefix)
                
        

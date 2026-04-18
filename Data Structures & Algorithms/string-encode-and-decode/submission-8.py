class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 
        print(s)
        while i < len(s):
            j = i 
            while s[j] != '#':
                j +=1 
            lenght = int(s[i:j])
            i += len(s[i:j]) + 1
            decoded.append(s[i:i + lenght])
            i += lenght
        
        return decoded

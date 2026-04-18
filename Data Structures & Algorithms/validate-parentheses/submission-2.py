class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                openBracket = stack.pop()
                
                if c == ')' and openBracket == '(':
                    pass
                elif c == '}' and openBracket == '{':
                    pass
                elif c == ']' and openBracket == "[":
                    pass
                else:
                    return False
        
        return len(stack) == 0
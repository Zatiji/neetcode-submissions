class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        last = -1
        stack = []

        for s in tokens:

            if s in operators:
                if s == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    result = num2 + num1
                    stack.append(result)
                elif s == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    result = num2 - num1
                    stack.append(result)
                elif s == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    result = num2 * num1
                    stack.append(result)
                elif s == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    result = int(num2 / num1)
                    stack.append(result)
            
            else:
                stack.append(int(s))
        
        return stack.pop()

                
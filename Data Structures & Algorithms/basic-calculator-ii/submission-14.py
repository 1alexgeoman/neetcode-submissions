class Solution:
    def symbol(self, a,b,op):
        if op == "*":
            return a*b
        elif op == "+":
            return a+b
        elif op == "/":
            return a//b
        if op == "-":
            return a-b
    
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        last_op = "+"
        operators = {"+", "-", "*", "/"}
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            # Process if it's an operator OR the last character
            if char in operators or i == len(s) - 1:
                if last_op == "+":
                    stack.append(current_num)
                elif last_op == "-":
                    stack.append(-current_num)
                elif last_op == "*":
                    stack.append(stack.pop() * current_num)
                elif last_op == "/":
                    stack.append(int(stack.pop() / current_num))
                
                # Update for the next number
                last_op = char
                current_num = 0
                
        return sum(stack)




# sol = Solution()
# sol.calculate("352+43/78   -2")
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
        s = "".join(s.split())
        stack = []
        counter = 0
        
        while counter<len(s):
            k = ""
            while counter<len(s) and s[counter].isdigit():
                k+=s[counter]
                counter+=1
            
            if k:
                stack.append(k)
            
            if counter<len(s):
                stack.append(s[counter])
                counter+=1

        print(stack)

        loop = 0
        while loop!= len(stack):
            if stack[loop] =="*" or stack[loop] =="/":
                beforeNum = int(stack[loop-1])
                afterNum = int(stack[loop+1])
                stack[loop-1] = self.symbol(beforeNum, afterNum, stack[loop])
                del stack[loop+1]
                del stack[loop]
                loop = loop-1
            loop+=1
        
        loop=0
        while loop!= len(stack):
            if stack[loop] =="+" or stack[loop] =="-":
                beforeNum = int(stack[loop-1])
                afterNum = int(stack[loop+1])
                stack[loop-1] = self.symbol(beforeNum, afterNum, stack[loop])
                del stack[loop+1]
                del stack[loop]
                loop = loop-1
            loop+=1
        
        return int(stack[0])




# sol = Solution()
# sol.calculate("352+43/78   -2")
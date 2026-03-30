class Solution:
    def isValid(self, s: str) -> bool:
        valid = ["{","[","("]
        notValid = ["}","]",")"]
        stack = []

        if s[0] not in notValid:
            for item in s:
                if item in valid:
                    stack.append(item)
                else:
                    if len(stack)==0:
                        return False
                    current = stack.pop()
                    if current == "{" and item != "}":
                        return False
                    elif current == "[" and item != "]":
                        return False
                    elif current == "(" and item != ")":
                        return False
            if len(stack)!=0:
                return False
            return True
        return False
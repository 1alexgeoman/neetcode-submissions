class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        found = {}
        if len(s) !=  len(t):
            return False

        for letter in s:
            if letter in found:
                found[letter] +=1
            else:
                found[letter] = 1
        print (found.values())
        for letter in t:
            if letter in found:
                found[letter] -=1
        print (found.values())
        for item in found.values():
            if item != 0:
                return False
        
        return True
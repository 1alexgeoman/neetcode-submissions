class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_chars = []          # step 1: create an empty list to store valid characters

        for ch in s:           # step 2: loop through every character
            if ch.isalnum():      # step 3: check if character is a letter or number
                clean_chars.append(ch)   # step 4: keep it if alphanumeric

        s = ''.join(clean_chars).lower()

        print(s)
        for x in range (0,len(s)//2):
            if s[x] != s[len(s)-1- x]:
                print(s[x],s[len(s)-1- x])
                return False
        return True
        
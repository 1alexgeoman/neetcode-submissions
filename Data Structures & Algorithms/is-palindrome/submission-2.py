class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_chars = []

        for ch in s:
            if ch.isalnum():
                clean_chars.append(ch)

        s = ''.join(clean_chars).lower()

        print(s)
        for x in range (0,len(s)//2):
            if s[x] != s[len(s)-1- x]:
                print(s[x],s[len(s)-1- x])
                return False
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        r = s[::-1]

        l = len(s)

        for i in range(l):
            if (r[i] == s[i]):
                continue
            else:
                return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()
        if len(s) % 2 != 0:
            s = s[:len(s) // 2] + s[(len(s) // 2) + 1:]
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = "".join([c for c in s.lower() if c in alphabet])
        return s == s[::-1]
        
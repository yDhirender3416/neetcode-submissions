class Solution:
    def isPalindrome(self, s: str) -> bool:
        pstring=[char.lower() for char in s if char.isalnum()]
        return pstring==pstring[::-1]
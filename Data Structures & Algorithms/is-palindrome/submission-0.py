class Solution:
    def isPalindrome(self, s: str) -> bool:
        adjusted = ""
        for c in s.lower():
            if c in "abcdefghijklmnopqrstuvwxyz1234567890":
                adjusted += c
        for i, c in enumerate(adjusted):
            print(adjusted[i])
            print(adjusted[len(adjusted)-i-1])
            if adjusted[i] != adjusted[len(adjusted)-i-1]:
                return False
        return True
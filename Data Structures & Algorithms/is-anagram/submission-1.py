class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1Dict = {}
        word2Dict = {}
        for char in s:
            if char in word1Dict:
                word1Dict[char] = word1Dict[char] + 1
            else:
                word1Dict[char] = 1
        for char in t:
            if char in word2Dict:
                word2Dict[char] = word2Dict[char] + 1
            else:
                word2Dict[char] = 1
        for key in list(word1Dict.keys()):
            if(key not in word2Dict or word2Dict[key] != word1Dict[key]):
                return False
        for key in list(word2Dict.keys()):
            if(key not in word1Dict or word2Dict[key] != word1Dict[key]):
                return False
        return True
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using dictionary
        return Counter(s)==Counter(t)
        
        
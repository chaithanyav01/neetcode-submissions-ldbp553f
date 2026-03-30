class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        def freq(s):
            mp = {}
            for i in s:
                if i not in mp:
                    mp[i] = 0
                mp[i] += 1
            return mp
        return freq(s) == freq(t)
        
        


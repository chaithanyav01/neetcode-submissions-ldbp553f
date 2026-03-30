class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(a):
            hashmap = {}
            for i in a:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            return hashmap
            
        return freq(s) == freq(t)
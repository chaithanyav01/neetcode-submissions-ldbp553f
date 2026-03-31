class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     charset =set()
        #     for j in range(i,len(s)):
        #         if s[j] in charset:
        #             break
        #         charset.add(s[j])
        #         res = max(res,len(charset))
        # return res

        res = 0
        i =0
        charset= set()

        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1
            charset.add(s[j])
            res = max(res,j-i+1)
        return res


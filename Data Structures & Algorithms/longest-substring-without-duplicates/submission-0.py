class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res = 0
        # for i in range(len(s)):
        #     charset = set()
        #     for j in range(i,len(s)):
        #         if s[j] in charset:
        #             break
        #         charset.add(s[j])
        #     res = max(res,len(charset))
        # return res

        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res,r-l+1)
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc+=str(len(s))+"$"+s
        print(enc)
        return enc
            

    def decode(self, s: str) -> List[str]:
        deco=[]
        i=0
        while i<len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])
            i = j+1
            deco.append(s[i:i+length])
            i += length
        return deco

            


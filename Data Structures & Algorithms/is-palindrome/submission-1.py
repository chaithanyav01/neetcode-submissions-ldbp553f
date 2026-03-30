class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = ""
        for i in s:
            if i.isalnum():
                filtered+=i.lower()
        
        i = 0
        j = len(filtered)-1

        while i<j:
            if filtered[i] != filtered[j]:
                return False
            else:
                i+=1
                j-=1
        return True


        
        
        

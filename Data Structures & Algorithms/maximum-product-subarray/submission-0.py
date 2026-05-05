class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = maxProd = minProd =  nums[0]

        for i in range(1,len(nums)):
            if nums[i] <0 :
                maxProd, minProd =  minProd, maxProd
            
            maxProd =  max(nums[i], nums[i]*maxProd)
            minProd =  min(nums[i], nums[i]*minProd)

            ans =  max(ans, maxProd)
        return ans
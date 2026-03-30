class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right=len(nums)-1

            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s==0:
                    res.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    left+=1
                    right-=1
                elif s>0:
                    right-=1
                else:
                    left+=1
        print(res)
        return [list(v) for v in res]
                    
        
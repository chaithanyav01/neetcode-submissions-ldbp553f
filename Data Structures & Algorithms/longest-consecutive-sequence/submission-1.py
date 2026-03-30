class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        long =0
        for num in nums:
            if num-1 not in nums:
                l =0
                while num in nums:
                    l +=1
                    num += 1
                long = max(long,l)
        return long




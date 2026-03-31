class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for idx,num in enumerate(nums):
        #     if num == target:
        #         return idx
        # return -1

        left = 0
        right = len(nums)-1
        while left<=right:
            mid = int(left+(right-left)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left +=1
        return -1
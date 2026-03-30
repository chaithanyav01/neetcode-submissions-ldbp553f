class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left =0 
        right = n-1
        max_water = 0

        while left<right:
            width = right-left
            height = min(heights[left],heights[right])
            current_water = width*height
            max_water = max(max_water,current_water)

            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
            
            

        
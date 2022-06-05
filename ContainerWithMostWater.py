class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,(n-1)
        max_area = (r-l)*min(height[l],height[r])
        while l<r:
            min_ht = min(height[l],height[r])
            area = min_ht*(r-l)
            max_area = max(area,max_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area

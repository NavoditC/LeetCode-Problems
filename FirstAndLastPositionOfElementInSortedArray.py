class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,h = 0,n-1
        left_pos = -1
        right_pos = -1
        while l<=h:
            mp = (l+h)//2
            if nums[mp] == target:
                if mp == 0 or nums[mp-1]!=target:
                    left_pos = mp
                    break
                else:
                    h = mp-1
            elif target>nums[mp]:
                l = mp+1
            else:
                h = mp-1
        l,h = 0,len(nums)-1
        while l<=h:
            mp = (l+h)//2
            if nums[mp] == target:
                if mp == (n-1) or nums[mp+1]!=target:
                    right_pos = mp
                    break
                else:
                    l = mp+1

            elif target>nums[mp]:
                l = mp+1
            else:
                h = mp-1
        return [left_pos,right_pos]
        

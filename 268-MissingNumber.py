class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        req_sum = (n*(n+1))//2
        arr_sum = sum(nums)
        if arr_sum < req_sum:
            ele = req_sum - arr_sum
        else:
            if 0 in nums:
                ele = n+1
            else:
                ele = 0
        return ele


        

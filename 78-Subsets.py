class Solution:
    def sub(self,nums,res,index,t):
        if index==len(nums):
            res.append(t[:])
            return
        self.sub(nums,res,index+1,t)
        t.append(nums[index])
        self.sub(nums,res,index+1,t)
        t.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        t =[]
        self.sub(nums,res,0,t)
        return res

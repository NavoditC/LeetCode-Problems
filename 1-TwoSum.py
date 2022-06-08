class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            if (target-num) in d:
                i2=d[target-num]
                return [i,i2]
            else:
                d[num]=i

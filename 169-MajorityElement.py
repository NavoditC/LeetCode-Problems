from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
            if d[num]>n/2:
                return num
        return 0

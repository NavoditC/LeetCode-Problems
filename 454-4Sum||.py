
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        s1 = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s = nums1[i]+nums2[j]
                if s in s1:
                    s1[s] += 1
                else:
                    s1[s] = 1
        s2 = {}
        c = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                s = -(nums3[i]+nums4[j])
                if s in s1:
                    c += s1[s]

        return c
        

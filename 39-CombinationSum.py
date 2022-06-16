class Solution:
    def comb(self,candidates,target,part,res,i):
        if target==0:
            res.append(part[:])
            return
        if target<0 or i == len(candidates):
            return

        part.append(candidates[i])
        self.comb(candidates,target-candidates[i],part,res,i)
        part.pop()
        self.comb(candidates,target,part,res,i+1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        part = []
        self.comb(candidates,target,part,res,0)
        return res

        

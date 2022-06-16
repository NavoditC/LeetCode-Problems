class Solution:
    def comb(self,digits,index,res,arr,t):
        if index == len(digits):
            if t!="":
                res.append(t)
            return
        digit = int(digits[index])
        t1=t
        for ch in arr[digit]:
            t1+=ch
            self.comb(digits,index+1,res,arr,t1)
            t1=t

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        t = ""
        arr = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        self.comb(digits,0,res,arr,t)
        return res
        

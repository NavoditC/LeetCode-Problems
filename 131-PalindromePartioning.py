class Solution:
    def part(self,s,index,part,res):
        n = len(s)
        if index==n:
            res.append(part[:])
            return
        for i in range(index,n):
            s1 = s[index:i+1]
            if self.isPalin(s1):
                part.append(s1)
                self.part(s,i+1,part,res)
                part.pop()

    def isPalin(self,s):
        n = len(s)
        i,j = 0,n-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        self.part(s,0,part,res)
        return res
        

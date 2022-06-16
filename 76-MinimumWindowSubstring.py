from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        ds = defaultdict(int)
        for ch in t:
            dt[ch]+=1
        want = len(t)
        have = 0
        l,r = 0,0
        left,right = 0,0
        min_len = float('inf')
        while r<len(s):
            if s[r] in t:
                if ds[s[r]]<dt[s[r]]:
                    have+=1
                ds[s[r]]+=1

            while have == want:
                if (r-l+1)<min_len:
                    min_len = r-l+1
                    left = l
                    right = r
                if s[l] not in t:
                    pass
                else:
                    ds[s[l]]-=1
                    if ds[s[l]]<dt[s[l]]:
                        have-=1
                l+=1
            r+=1
        if min_len!=float('inf'):
            return s[left:right+1]
        else:
            return ""



        

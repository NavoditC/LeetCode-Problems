class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        max_len = 0
        l,r = 0,0
        seen={}
        while l<n and r<n:
            ch=s[r]
            if ch not in seen:
                seen[ch] = r
            else:
                l = max(l,seen[ch]+1)
                seen[ch]=r

            max_len = max(max_len,r-l+1)
            r += 1
        return max_len

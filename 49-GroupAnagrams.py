
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        d={}
        for word in strs:
            word_hash = "".join(sorted(word))
            if word_hash not in d:
                d[word_hash] = [word]
            else:
                d[word_hash].append(word)
        ans=[]
        for (k,v) in d.items():
            ans.append(v)
        return ans

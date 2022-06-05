class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i,j = 0,len(people)-1
        n = j+1
        c = 0
        while j>i:
            if (people[j]+people[i])>limit:
                j-=1
            else:
                j-=1
                i+=1
            c+=1
        if j == i:
            c+=1
        return c

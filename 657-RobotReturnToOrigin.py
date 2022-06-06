class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for ch in moves:
            if ch=='L':
                x-=1
            elif ch=='R':
                x+=1
            elif ch=='U':
                y+=1
            else:
                y-=1
        return (x==0 and y==0)



        

class Solution:
    def exists(self,word,board,index,m,n,aux):
        if index==len(word):
            return True
        ch = word[index]
        (i,j)= aux[-1]
        if (j-1)>=0 and board[i][j-1]==ch and (i,j-1) not in aux:
            aux.append((i,j-1))
            x = self.exists(word,board,index+1,m,n,aux)
            if x==False:
                aux.pop()
            else:
                return True

        if (i-1)>=0 and board[i-1][j]==ch and (i-1,j) not in aux:
            aux.append((i-1,j))
            x = self.exists(word,board,index+1,m,n,aux)
            if x==False:
                aux.pop()
            else:
                return True

        if (j+1)<n and board[i][j+1]==ch and (i,j+1) not in aux:
            aux.append((i,j+1))
            x = self.exists(word,board,index+1,m,n,aux)
            if x==False:
                aux.pop()
            else:
                return True

        if (i+1)<m and board[i+1][j]==ch and (i+1,j) not in aux:
            aux.append((i+1,j))
            x = self.exists(word,board,index+1,m,n,aux)
            if x==False:
                aux.pop()
            else:
                return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        aux = []
        ch = word[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == ch:
                    aux.append((i,j))
                    ans = self.exists(word,board,1,m,n,aux)
                    if ans==True:
                        return True
                    aux.pop()
        return False
        

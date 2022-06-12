class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if st==[]:
                    return False
                else:
                    ch1 = st.pop()
                    if (ch1,ch) not in [('(',')'),('{','}'),('[',']')]:
                        return False
        return st==[]

        

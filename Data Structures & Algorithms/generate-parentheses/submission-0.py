class Solution:
    def isvalid(self, s: str) -> bool:
        st = deque()
        for x in s:
            if x == '(':
                st.append(x)
            else:
                if not st:
                    return False
                st.pop()
        return True if not len(st) else False
        


    def rec(self, i:int, s: str, n: int) -> None:
        if i ==2*n:
            if self.isvalid(s):
                self.ans.append(s)
            return
        
        self.rec(i+1, s+'(', n)
        self.rec(i+1, s+')', n)
        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []  #creates and instance variable for the class. so each object has this variable. 
                       # this can be accessed in all methods [like rec()]
        self.rec(0, "", n)
        return self.ans


    
        
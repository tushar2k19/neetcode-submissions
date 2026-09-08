class Solution:
    def encode(self, strs: List[str]) -> str:
        st = ""
        for x in strs:
            st+=str(len(x))
            st+=","
        st+="#"
        for x in strs:
            st+=x
        return st

    def decode(self, s: str) -> List[str]:
        print(s)
        p1=""
        c = 0
        for i in range(len(s)):     #      _
            if s[i]=='#':             #     |
                c+=1                    #   |
                break                    #  |
            p1+=s[i]                   #    | -> p1, p2 = s.split('#', 1)
            c+=1                     #      |   (split by #, max split=1)
        p2=s[c:len(s)]           #          |
                                 #         _|
        
        sz = p1.split(',')
        sz.pop()
        sz = [int(x) for x in sz]
        print(p1,p2,sz)
        ans = []
        i = 0
        for x in sz:
            s1=''
            while x:
              s1+= p2[i]
              i+=1
              x-=1
            ans.append(s1)
            print(s1)
        print(ans)
        return ans
        


        return ["a"]
        
        


        
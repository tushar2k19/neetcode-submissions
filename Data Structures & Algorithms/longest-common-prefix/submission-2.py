class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        ans= ""
        idx = 0
        mn = 300;
        flag = 0
        for x in strs:
            mn = min(mn, len(x))
        print(mn)
        while(mn!=0):
            ch = ''
            for i,x in enumerate(strs):
                if i==0:
                    ch = x[idx]
                else:
                    if x[idx] != ch:
                        flag = 1
                        break
            print(ch, "=>",ans)
            if flag==1:
                break
            ans+=ch
            idx+=1
            mn-=1
        
        return ans
    
        
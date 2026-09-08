class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for x in strs:
            res+=str(len(x))
            res+=","
        res+="#"
        for x in strs:
            res+=x
        print("res=", res)
        return res
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        str1, str2 = "",""
        for i in range(len(s)):
            if s[i]=='#':
                str1 = s[0:i]
                str2 = s[i+1: len(s)]
                break;
        print(str1,"==",str2)
        # sz = list(map(int, str1.split(','))) //apply filter to check empty string
        sz = [int(x) for x in str1.split(',') if x!='']
        print(sz, str1, str2)

        st = 0;
        ans = []
        for x in sz:
            temp = str2[st:st+x]
            # print(x, temp)
            ans.append(temp)
            st+=x
            # print(ans)
        return ans
        
        
        


        
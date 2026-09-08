class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for x in strs:
            enc+=str(len(x))
            enc+=","
        enc = enc[0:len(enc)-1]    #enc[:-1]  also works
        enc+="#"
        for x in strs:
            enc+=str(x)
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        if len(s)<=0:
            return []
        p1,p2 = "", ""
        for i in range(len(s)):
            if s[i]=='#':
                p1 = s[:i]
                p2 = s[i+1:]
                break
        lens = p1.split(',')
        lens = [int(x) for x in lens if x]
        # print(p1,p2, lens)

        i = 0
        ans = []

        for x in lens:
            word = p2[i:i+x]
            i=i+x
            ans.append(word)
        # print(ans)
        return ans

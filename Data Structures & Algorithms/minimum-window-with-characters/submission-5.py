class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1, mp2 = defaultdict(int), defaultdict(int)
        
        j,n = 0, len(s)
        ans, ch1, ch2 = "", 0,0
        flag = True

        for x in t:
            mp2[x]+=1
            ch2+=1

        min_len = math.inf
        st = 0
        for i in range(n):
            if s[i] in mp2:
                mp1[s[i]]+=1
                if mp1[s[i]]<=mp2[s[i]]:
                    ch1+=1

            # print(i, mp1)
            while ch1==ch2:
                if s[j] in mp1:
                    mp1[s[j]]-=1
                    if mp1[s[j]]<mp2[s[j]]:
                        ch1-=1

                if i-j+1<min_len:
                    min_len = i-j+1
                    st = j
                # print(i,j,st, min_len)
                j+=1
        # print(st,min_len)
        return "" if min_len==math.inf else s[st:st+min_len]
        # return ans


        
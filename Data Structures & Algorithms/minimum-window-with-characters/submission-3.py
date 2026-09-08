class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1, mp2 = defaultdict(int), defaultdict(int)
        
        j,n = 0, len(s)
        ans, ch1, ch2 = "", 0,0
        flag = True

        for x in t:
            mp2[x]+=1
            ch2+=1

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

                if flag:
                    flag = False
                    ans = s[j:i+1]
                else:
                    if (i-j+1)<len(ans):
                        ans = s[j:i+1]
                # print("j = ", j)
                j+=1
        return ans


        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j,n = 0,0,len(s)
        mp = defaultdict(int)
        ans = 0
        while i < n:
            c = s[i]
            mp[c]+=1
            mx_c = max(mp, key=mp.get, default='') 

            while (i-j+1)-mp[mx_c]-k>0:
                mp[s[j]]-=1
                mx_c = max(mp, key=mp.get, default='') 
                j+=1
            
            print(i,j)
            ans = max(ans, i-j+1)
            i+=1
            
        return ans
        
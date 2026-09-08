class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,n = 0,0, len(s)
        mp = defaultdict(int)

        ans = 0
        while i<n:
            c = s[i]
            if c in mp and mp[c]>=j:
                j = mp[c]+1
            mp[c] = i
            ans = max(ans, i-j+1)
            i+=1
        return ans
            

        
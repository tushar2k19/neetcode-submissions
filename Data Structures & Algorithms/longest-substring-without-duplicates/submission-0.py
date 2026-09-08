class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        ans = 0
        mp = defaultdict(lambda: -1)
        for k,x in enumerate(s):
            if x in mp:
                pos = mp[x] + 1
                for idx in range(j, pos):
                    del mp[s[idx]]
                    i+=1
                j=i

            mp[x] = k
            ans = max(ans, len(mp))
        return ans


        
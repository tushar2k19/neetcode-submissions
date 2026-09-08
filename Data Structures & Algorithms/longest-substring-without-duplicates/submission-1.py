class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        ans = 0
        if len(s)==1:
            return 1
        mp = defaultdict(lambda: -1)
        for j,x in enumerate(s):
            if x in mp and mp[x]>=i: 
                i=mp[x]+1

            mp[x] = j
            ans = max(ans, j-i+1)
        return ans


        
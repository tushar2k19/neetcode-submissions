class Solution:
    def maxProfit(self, p: List[int]) -> int:
        b,s = 0,0

        n = len(p)
        ans = 0
        for i in range(1,n):
            if p[i]>=p[i-1]:
                s = i
            else:
                s = i
                if p[i]<p[b]:
                    b=i
            ans = max(ans, p[s] - p[b])
        return ans 
                


        
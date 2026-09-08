class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        i,j = 0, n-1

        # left, right = [0]*n, [0]*n
        # left[0], right[n-1] = h[0], h[n-1]

        # for i in range(1,n):
        #     left[i] = max(left[i-1], h[i])
        #     right[n-i-1] = max(h[n-i-1], right[n-i])



        # print(left, right)
        # ans = 0
        # for i in range(n):
        #     ans += min(left[i], right[i]) - h[i]
        # return ans

        lmax, rmax,ans = -1,-1,0
        while(i<j):
            lmax = max(lmax, h[i])
            rmax = max(rmax, h[j])

            if h[i]<h[j]:
                ans+=min(lmax, rmax) - h[i]
                i+=1
            else:
                ans+=min(lmax, rmax) - h[j]
                j-=1
        print(ans)
        return ans



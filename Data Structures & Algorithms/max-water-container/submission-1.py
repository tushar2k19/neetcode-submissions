class Solution:
    def maxArea(self, h: List[int]) -> int:
        area = 0
        l = 0
        r = len(h)-1
        while l<r:
            ar = min(h[l], h[r])*(r-l)
            area = max(area, ar)

            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return area
        
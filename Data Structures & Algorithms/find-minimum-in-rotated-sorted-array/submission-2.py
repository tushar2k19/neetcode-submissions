class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r,m = 0, n-1, 0

        while l<r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        
        # print(l,r,m)
        return nums[l]

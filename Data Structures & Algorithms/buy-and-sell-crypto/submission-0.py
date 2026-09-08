class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        ans = 0
        b,s = 0,0
        n = len(nums)
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                s = i
                ans = max(ans, nums[s]-nums[b])
            else:
                if nums[b]>nums[i]:
                    b = i
        return ans
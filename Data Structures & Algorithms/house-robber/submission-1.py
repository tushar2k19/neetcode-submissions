class Solution:
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        prev2 = nums[0]
        if n==1:
            return nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, n):
            a = prev2 + nums[i]
            b = prev

            prev2 = prev
            prev = max(a,b)
        return prev
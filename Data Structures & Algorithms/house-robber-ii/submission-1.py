class Solution:
    def fn(self, nums: List[int]) -> int:
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
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        a = nums[0:n-1]
        b = nums[1:n]
        return max(self.fn(a), self.fn(b))

        
class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] *n
        right = [0]*n
        left[0] = nums[0]
        right[n-1] = nums[n-1]

        for i in range(1,n):
            print(i)
            left[i] = max(left[i-1], nums[i])
            right[n-i-1] = max(right[n-i], nums[n-i-1])
        print(left, right)
        ans = 0
        for i in range(0,n):
            # print(left[i], right[i], nums[i], "-> ", min(left[i], right[i]) - nums[i])
            ans+=min(left[i], right[i]) - nums[i]
        return ans
    
        
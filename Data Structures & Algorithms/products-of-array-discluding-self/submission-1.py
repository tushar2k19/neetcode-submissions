class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        n= len(nums)
        for i in range(n):
            if i!=0:
                left[i] = left[i-1]*nums[i-1]
            # if i!=n-1 :
                right[n-i-1] = right[n-i]*nums[n-i]
            print(left, right)
        for i in range(n):
            nums[i] = left[i]*right[i]
        return nums
            



    
        



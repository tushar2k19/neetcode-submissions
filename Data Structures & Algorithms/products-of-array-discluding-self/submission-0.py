class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        count=0
        for x in nums:
            if x==0 and count==0:
                count+=1
            elif x!=0 and count == 0:
                pro*=x
            elif x==0 and count!=0:
                pro = 0
                break
            else:
                pro*=x

        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = int(pro)
            else:
                if count==0:
                    nums[i] = int(pro/nums[i])
                else:
                    nums[i] = 0
        return nums
    
        
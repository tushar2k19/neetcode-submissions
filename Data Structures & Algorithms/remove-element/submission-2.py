class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)
        while i<j:
            if(nums[i]==val):
                nums[i]=nums[j-1]
                j-=1
                i-=1
            i+=1
        return j



        
        
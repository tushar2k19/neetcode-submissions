class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
    
        l,r,ans= 0,n-1,0
        lmax,rmax = 0,0


        while l<r:
            if(nums[l]>nums[r]):
                rmax= max(rmax, nums[r])
                ans+=rmax - nums[r]        #bcz we are shifting the index jiski value kam h. so for any i, rmax will be greater than 0 se 'l' tak ki saari values and same goes for "else" condition below
                r-=1
            else:
                lmax = max(lmax, nums[l])
                ans+= lmax - nums[l]
                l+=1
        
        

        return ans
    
        
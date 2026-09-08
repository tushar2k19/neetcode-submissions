class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for k in range(len(nums)):
            l,r = 0, len(nums)-1
            
            while l<=r:
                if l==k:
                    l+=1
                elif r==k:
                    r-=1
                else:
                    if nums[k] + nums[l]+nums[r] ==0 and l!=r:
                        ans.add(tuple(sorted([nums[l],nums[r],nums[k]])))
                        l+=1 
                        r-=1
                    elif nums[k] + nums[l]+nums[r] > 0:
                        r-=1
                    else:
                        l+=1
                    
    
            # print (k, l, r)
            
        abc = [list(x) for x in ans] 
        return abc



        
        
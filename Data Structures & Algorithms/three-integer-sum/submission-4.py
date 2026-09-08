class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for k,x in enumerate(nums):
            i,j = k+1, len(nums)-1

            if k>0 and nums[k]==nums[k-1]:
                continue

            while i<j:
                total = nums[i] + nums[j] + nums[k]
                if i!=j and total == 0:
                    tp = tuple(sorted([nums[i], nums[j], nums[k]]))
                    ans.add(tp)

                    if nums[i+1]==nums[i]:
                        i+=1
                    if nums[j-1]==nums[j]:
                        j-=1
                    i+=1
                    j-=1
                elif total < 0:
                    i+=1
                else:
                    j-=1
        ans = [list(x) for x in ans]
        # print(ans)    
        return ans



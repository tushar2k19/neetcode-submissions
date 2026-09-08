class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums)

        mp = defaultdict(int)
        for x in nums:
            mp[x]=1
        print(mp)
        
        ans = 0
        
        for i in range(n):
            count = 0
            num = nums[i]
            print(nums[i]-1)
            if nums[i]-1 not in mp: 
                while 1:
                    if num in mp:
                        count+=1
                        ans = max(ans, count)
                        num+=1
                    else:
                        break
            ans = max(ans, count)
        return ans



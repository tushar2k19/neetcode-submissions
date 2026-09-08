class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for x in nums:
            mp[x]+=1
        ans = 0
        mx = 0

        for i,x in mp.items():
            if x > mx:
                mx = x
                ans = i
        
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0

        mp = defaultdict(bool)
        for x in nums:
            mp[x] = True
        
        msp = defaultdict(bool)
        for x in nums:
            if x-1 not in mp:
                msp[x] = True

        mx = -math.inf
        for x in msp.keys():
            num, count = x,1
            while num+1 in mp:
                num = num+1
                if num in mp:
                    count+=1
                else:
                    break
            mx = max(mx, count)
        return mx
        
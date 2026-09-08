class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for x in nums:
            if x in mp:
                return True
            else: 
                mp[x] = 0
        
        return False
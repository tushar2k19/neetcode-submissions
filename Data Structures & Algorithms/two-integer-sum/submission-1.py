class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,x in enumerate(nums):
            mp[x] = i
        
        for i,x in enumerate(nums):
            nu = target - x
            print(i, x, nu)
    
            if nu in mp:
                print("->", mp)
                if i != mp[nu]:
                    return [i, mp[nu]]
            
        return []
            
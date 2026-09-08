class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for x in nums:
            mp[x]+=1
        
        sorted_arr = sorted(mp.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):          
            ans.append(sorted_arr[i][0])
        return ans
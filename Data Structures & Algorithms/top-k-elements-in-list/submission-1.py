class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for x in nums:
            mp[x]+=1
        
        # sorted_arr = sorted(mp.items(), key=lambda item: item[1], reverse=True)
        # ans = []
        # for i in range(k):          
        #     ans.append(sorted_arr[i][0])
        # return ans

        heap = []   #[(1,1), (2,2), (3,3)]   3 coming 3 times
        for j,v in mp.items():
            heapq.heappush(heap, (v,j))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [y for x,y in heap]
    


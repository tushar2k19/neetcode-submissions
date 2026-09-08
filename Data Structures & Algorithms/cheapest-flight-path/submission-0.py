class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adl = [[] for x in range(n)]
        for x in flights:
            adl[x[0]].append((x[1],x[2]))
        
        pq = []
        heapq.heappush(pq, (0, 0, src))

        stops = [math.inf]*n

        while pq:
            top = heapq.heappop(pq)

            if top[2] == dst:
                return top[0]
            if top[1] > stops[top[2]]:
                continue
            stops[top[2]] = top[1]
            for x in adl[top[2]]:
                if top[1] <= k:
                    new_price = top[0] + x[1]
                    heapq.heappush(pq, (new_price, top[1] + 1, x[0]))
        return -1
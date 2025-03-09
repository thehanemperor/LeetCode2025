class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for x,y,cost in flights:
            if x not in adj:
                adj[x] = [(y,cost)]
            else:
                adj[x].append((y,cost))

        queue = deque([(src,0,0)])
        price = [float("inf")] * n
            

        while queue:
            curr,cost,step = queue.popleft()

            for nei in adj.get(curr,[]):
                
                location, charge = nei
                if step ==k+1:
                    break

                if cost + charge < price[location]:
                    price[location] = cost + charge
                    queue.append((location, price[location], step+1))

        return price[dst] if price[dst]!= float("inf") else -1
            
                 
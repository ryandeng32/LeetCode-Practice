### From Code Practice
* Alternative solution: 
* Graph Type: Weighted directed graph with no negative cycle 
* Min path in terms of edge weights -> Dijkstra's algorithm 

* Solution: 
* Want minimum cost
  * Shortest path in terms of costs
* 1. construct the graph (map of node to adjacent nodes) 
* 2. We can use BFS
  * initialize min_price to infinity 
  * in BFS queue we need (node, stops, cost so far) 
  * (do not stop at destination) When we reach dest just update the min price to get to it and continue
  * When exceed k stops -> stop exploring neighboring
  * while exploring neighbours if going to that neighbour has cost > current min_price, then stop 
  * if min_price is still infinity at the end, then return -1 

### Code
```python
class Solution: 
  def findCheapestPrice(self, n, flights, src, dst, K):
    # Construct graph
    graph = collections.defaultdict(list)
    for u, v, c in flights: 
      graph[u].append((v, c)) 
    
    # BFS
    queue = collections.deque([(src, 0, 0)])
    minCost = float('inf') 
    while queue: 
      node, stops, costSoFar = queue.popleft()
      if node == dst: 
        minCost = min(minCost, costSoFar) 
        continue
      if stops > K or costSoFar > minCost: 
        continue
      for nei, nc in graph[node]: 
        queue.append((nei, stops + 1, costSoFar + nc))
     return minCost if minCost != float('inf') else -1 
      
       
      
```

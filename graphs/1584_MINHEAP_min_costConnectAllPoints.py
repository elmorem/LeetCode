'''


You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected._ All points are connected if there is **exactly one** simple path between any two points.
- need to create a minmum spanning tree
- [[0,0],[2,2],[3,10],[5,2],[7,0]]****

> [!NOTE] Algo Summary
> 1. we're gogin to use a min heap to collect all the points, order them and then get the distance between each
> 2. initialize the min heap at (0,0)
> 3. each entry in the min heap is going to be the distance to the closest neighbor and the index
> 4. we add i to our seen set
> 5. and add that distance to the total distance
> 6. once we have that i set, we set xi, yi to points[i] a
> 7. then we use j to cycle through our edges
> 	1. if j insn't in see then xj, yj become points[j ] and
> 	2. we use this to get out nei_dist
> 	3. and push those values onto the heap (these are the values from the index (i) that was closest last time
> 8. return total distance
'''
def minCostConnectPoints(self, points: List[List[int]]) -> int:
	# need n-1 edges where n = len(pointssee)
	n = len(points)
	total_cost = 0
	seen = set()
	min_heap = [(0,0)]
	while len(seen) < n:
		dist, i = heapq.heappop(minheap)
		if i in seen:
			continue
		seen.add(i)
		total_cost += dist
		xi, yi = points[i]
		for j in range(n):
			if j not in seen:
				xj, yj = points[j]
				nei_dist = abs(xi-xj) + abs(yi -yj)
				heapq.heappush(min_heap, (nei_dist, j))
	return total_cost
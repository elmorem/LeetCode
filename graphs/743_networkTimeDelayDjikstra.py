'''
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the_ `n` _nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2

> [!NOTE] Algo Sumary
> Key: because we need the min time, we are going to use a min heap
> 1. initialize: min heap, adj graph, and a min times
> 2. min heap is initialized with a time of 0 and k is the node where we start
> 3. min times is essentially our visisted last and a place to hold all our final values 
> 4. Process:
> 	1. while min_heap
> 	2. start by popping of the heap the initial value
> 	3. check if it is in min_times
> 	4. if not, add it
> 	5. then we have a for loop that goes through any values in the graph at[i]
> 	6. to get the times from K to i we add whatever was there before to the value of that section
> 	7. Because we need to check if it is impossible for all the nodes to get the signal, we do a final check if len(min_times) == n: if not then we return -1
> 8. Else we return the max of the min_times
> 9. Time complexity is O(E + V log V) where E is the number of edges and V is the number of vertices
# 10. Space complexity is O(E + V) where E is the number of edges and V is the number of vertices
'''
from collections import defaultdict
import heapq
from typing import List, Tuple
def sol(times, n, k):
	graph = defaultdict(list)
	for u,v,time in times:
		graph[u].append((v, time))
	min_times = {}
	min_heap = [(0, k)]
	while min_heap:
		time_k_to_i, i = heapq.heappop(min_heap)
		if i in min_times:
			continue
		min_times[i] = time_k_to_i
		for nei, nei_time in graph[i]:
			if nei not in min_times:
				heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
	if len(min_times) == n:
		return max(min_times.values())
	else:
		return -1
# Test cases
print(sol([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
print(sol([[1,2,1],[2,3,2],[1,3,4]], 3, 1)) # 3
print(sol([[1,2,1],[2,3,2],[1,3,4]], 4, 1)) # -1
	
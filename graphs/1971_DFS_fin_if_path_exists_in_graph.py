'''
There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` _if there is a **valid path** from_ `source` _to_ `destination`_, or_ `false` _otherwise__._
**Input:** n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
**Output:** true

> [!NOTE] Algo Summary
> KEY: Whenever we have bidirectional graph we need to add both sides of the edges to adj graph
> 1. create a visited set
> 2. create the graph with default dict remembering to add both sides
> 3. initial condition if source == desination return True
> 4. now were gogin to run DFS
> 5. base case is that if i == destination we know there is a path and we return True
> 6. If that isn't true then we're gogin to go through the neighbors at graph[i]
> 	1. if it's not in visited add it
> 	2. then we run dfs(nei) if it's True return True 
> 	3. if we go through all the edges and not Ture then return False


'''
# dfs with recursion
def sol(n, edges, source, destination):
	visited = set()
	if source == destination:
		return True
	graph = defaultdict(list)
	for a, b in edges:
		graph[a].append(b)
		graph[b].append(a)
	visited.add(source)
	
	def dfs(i):
		if i == destination:
			return True
		#now we are going to look through all the nodes
		for nei_node in graph[i]:
			if nei_node not in visited:
				visited.add(nei_node)
				if dfs(nei_node):
					return True
		return False
	return dfs(source)
# iterative solution
def sol(n, edges, source, destination):
	visited = set()
	if source == destination:
		return True
	graph = defaultdict(list)
	for a, b in edges:
		graph[a].append(b)
		graph[b].append(a)
	visited.add(source)
	stack = [source]
	while stack:
		node = stack.pop()
		if node == destination:
			return True
		for nei_node in graph[node]:
			if nei_node not in seen:
				seen.add(nei_node)
				stack.append(nei_node)
	return False

# BFS
from collections import Deque 
def sol(n, edges, source, destination):
	
	if source == destination:
		return True
	graph = defaultdict(list)
	for a, b in edges:
		graph[a].append(b)
		graph[b].append(a)
	visited = set()
	visited.add(source)
	q = deque()
	q.append(source)
	while q:
		node = q.popleft()
		if node == destination:
			return True
		for nei_node in graph[node]:
			visited.add(nei_node)
			q.append(nei_node)
	return False
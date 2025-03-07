'''
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1'
Return `true` if you can finish all courses. Otherwise, return `false`.
**Example 1:**
**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

'''

def cycles(courses, numCourses):
	g = defaultdict(list)
	for a, b in courses:
		g[a].append(b)   # would this be the same as g[a] = b no, b/c there
		                #  might be more values
	UNVISITED = 0
	VISITING = 1
	VISITED = 2
	states = [UNVISITED for x in range(numCourses)]
	
	def dfs(node):
		state = states[node]
		if state == VISITED:
			return True
		if state == VISITING:
			return False
		states[node] = VISITING
		for nei in g[node]:
			if not dfs(nei):
				return False
		states[node] = VISITED
		return True

	# Base iteration
	for i in range(numCourses):
		if not dfs(i):
			return False
	return True
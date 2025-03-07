'''
### How it works
1. create an adjacency list for the graph
- Leetcode 210
	- the twist here is that we need to return the ordering of courses to finish all the classes and if it is impossible return an empty array
	- simple example:
		- N = 4
		- P = [[1,0], [2,0], [3,1], [3,2]
		- therefore 0 is a prereq for 1
		- 0 is a prereq for 2
		- 1 is a prereq for 3
		- 2 is a prereq for 3
		- so this is a valid order [0, 1,2,3]
		- this is what the adjacency list looks like: defaultdict(list, {1: [0], 2: [0], 3: [1, 2]})
	- Harder:
		- n = 6
		- p = [[2,0], [1,0],[0,3],[3,4],[3,5]]
		- here is the adjacency list:
		-  defaultdict(list, {2: [0], 1: [0], 0: [3], 3: [4, 5]})
		- order then: 4,5,,3,0,1,2

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`
Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
'''

def Schedule_2(prerequisites, numCourses):
	g = defaultdict(list)
	for a, b in courses:
		g[a].append(b)   
	result = []
	UNVISITED = 0
	VISITING = 1
	VISITED = 2
	states = [UNVISITED for x in range(numCCourses)]
	# True if no cycle. False if cycle 
	def dfs(i):
		if states[i] == VISITING:
			return False
		elif states[i] == VISITED:
			return True
		states[i] = VISITING
		for nei in g[i]:
			if not dfs(nei):
				return False
		states[i] = VISITED
		result.append(i)
		return True
	for i in range(numCourses):
		if not dfs(i):
			return []
	return result
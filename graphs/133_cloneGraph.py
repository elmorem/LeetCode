'''
 start by doing dfs on old graph collect all the nodes
Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.


> [!NOTE] Algo Summary
> 1. we are going to create a clone of the graph. start by doing a dfs on all the nodes
> 2. create a dict old_to_new that will clone the old one to the new one.
> 3. we must create the new nodes
> 4. create a visited set to track which ones we've added the the new dict
> 5. we make the stack and then cyce through at each one we create a new node 
> 6. then we need to do a second iteration through that will add the node.neighbors to the new dict
> 7. finally we just return old_to_new[start]


'''
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.value = val
		self.neighbors = neighbors if neihbors else []

class Solution:
	def clone_graph(self, node):
		if not node:
			return None
		start = node
		old_to_new = {}
		stk = [node]
		visited = set()
		visited.add(start)
		while stk:
			node = stk.pop()
			# the key here is that we are making a new node
			old_to_new[node] = Node(val=node.val)
			for nei in node.neighbors:
				if nei not in visited:
					visited.add(nei)
					stk.append(nei)
		# In the first iteration we add all of the nodes
		for old_node, new_node in old_to_new.items():
		#Then here we are adding all the node.neighbors
			for nei in old_node.neighbors:
				new_nei = old_to_new[nei]
				new_node.neighbors.append(new_nei) 
		return old_to_new[start]

# Time complexity is O(n) where n is the number of nodes
# Space complexity is O(n) where n is the number of nodes
# This is because we are storing the old_to_new dict and the visited set


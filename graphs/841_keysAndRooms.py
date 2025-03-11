'''
There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of **distinct keys** in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` _if you can visit **all** the rooms, or_ `false` _otherwise_.
**Example 1:**
**Input:** rooms = [[1],[2],[3],[]]
**Output:** true
**Explanation:** 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

> [!NOTE] Algo Summary
> Key: the key insight here is if we do a dfs and the len of our visited set is == to the len(rooms) then we have visisted all the rooms
> 1. initialize a visited set
> 2. dfs function passes in index
> 	1. add the index to visisted
> 	2. then cycle through any keys in the rooms[room] if that one isn't in visisted
> 3. call dfs on index 0
> 4. finally check if the len of visited is equal to the length of rooms
> 5. Time complexity is O(n) where n is the number of rooms
> 6. Space complexity is O(n) where n is the number of rooms
> 7. This is because we are storing the visited set and the stack
'''
def sol(rooms):
        visited = set()
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                # the rooms[room] works because they are a list
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited) == len(rooms)
# Test cases
print(sol([[1],[2],[3],[]])) # True
print(sol([[1],[2],[3],[4],[]])) # True
print(sol([[1,3],[3,0,1],[2],[0]])) # False

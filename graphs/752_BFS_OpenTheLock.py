'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

**Example 1:**

**Input:** deadends = ["0201","0101","0102","1212","2002"], target = "0202"
**Output:** 6
**Explanation:** 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

> [!NOTE] Algo Summary
> Key for each of the 4 options on the wheek we are going to have 2 options each time (+1 or -1), which means for each one of those 8 we re going to have 8 more options
> so we keep a visited set with the lock value and the # of moves it takes
> 1. if we reach a position we have already seen, we break
> 2. if we reach a combination in the deadends list, we break
> 3. BECAUSE THIS IS A SHORTEST PATH ALGORITHM, we use BFS. we could use backtacking, but i wouldn't be the most efficient
> 4. NOTE: There is a useful trick int he getChildren helper function that allows us to increment or decrement by 1 each time
> 5. Initialize the start, the deck (our q) and the visited set
> 6. add deadends to the visisted set
> 7. after this just basic BFS.  Popleft 
> 8. if we reach our target return the number of turns
> 9. then get Children and for each child in getChildren add them to the q and the visited set IF they are not already in there
> 10. finally return -1 if we never reach the target

'''
from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def getChildren(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+ 1) %10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i])-1+10) %10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        start = "0000"
        if start in deadends:
            return -1
        q = deque()
        q.append([start, 0])
        visited = set(deadends) # add deadends to the 
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            # get all 8 of the children of whever the state was at pop
            for child in getChildren(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, turns+1])
        return -1
# Test cases
sol = Solution()
print(sol.openLock(["0201","0101","0102","1212","2002"], "0202")) # 6
print(sol.openLock(["8888"], "0009")) # 1
print(sol.openLock(["0000"], "8888")) # -1
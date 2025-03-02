'''
I NTUTION:  basically if we do everything optimally, then we will know that ALICE WILL ALWAYS WIN
Alice and Bob play a game with piles of stones. There are an **even** number of piles arranged in a row, and each pile has a **positive** integer number of stones `piles[i]`.

The objective of the game is to end with the most stones. The **total** number of stones across all the piles is **odd**, so there are no ties.

Alice and Bob take turns, with **Alice starting first**. Each turn, a player takes the entire pile of stones either from the **beginning** or from the **end** of the row. This continues until there are no more piles left, at which point the person with the **most stones wins**.

Assuming Alice and Bob play optimally, return `true` _if Alice wins the game, or_ `false` _if Bob wins_.

**Example 1:**

**Input:** piles = [5,3,4,5]
**Output:** true
**Explanation:** 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

'''
from typing import List
def stoneGame(self, piles: List[int]) -> bool:
    # dp solution if there actually was a possibility of alice losing
    dp  = {} # subarray piles (l, r) --> max alice total
    # Return the total max that alice can return
    n = len(piles)
    def dfs(l,r):
        if l>r:
            return 0
        if(l,r) in dp:
            return dp[(l,r)]
        
        even = True if (r-l)%2 else False
        left = piles[l] if even else 0 
        right = piles[r] if even else 0 

        dp[(l,r)] = max(dfs(l+1, r) + left, dfs(l, r-1) + right)
        return dp[(l,r)]

    alice = dfs(0, n-1)  
    bob = sum(piles)- alice
    return True if alice > bob else False 

print(stoneGame(0, [5,3,4,5])) # True
print(stoneGame(0, [1,2,3,4,5,6])) # True
    
    

'''
    alice = []
    bob = []
    n = len(piles)
    odd, even = 0, 0
    for i in range(len(piles)):
        if i % 2 == 0:
            even += piles[i]
        else:
            odd += piles[i]
    alice.append(max(odd, even))
    bob.append(min(odd,even))
    print (f"{sum(bob) = }")
    print (f"{sum(alice) = }")
    return False if sum(bob) > sum(alice) else True 
'''
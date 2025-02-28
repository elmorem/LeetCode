'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sides = [0 for x in range(4)]
        perimeter = sum(matchsticks)
        side_size = perimeter // 4
        if perimeter % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == n:
                return True
            for j in range(4):  # j is gogin to serve here as each of the 4 sides
                if sides[j] + matchsticks[i]<= side_size:  
                    # basically here as long as we don't have a side that is longer than our needed length
                    # we're going to do the backtracking part
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)

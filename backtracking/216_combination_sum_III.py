'''
Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:
- Only numbers `1` through `9` are used.
- Each number is used **at most once**.
Return _a list of all possible valid combinations_. The list must not contain the same combination twice, and the combinations may be returned in any order.
**Example 1:**
**Input:** k = 3, n = 7
**Output:** [[1,2,4]]
**Explanation:**
1 + 2 + 4 = 7
There are no other valid combinations.
**Example 2:**
**Input:** k = 3, n = 9
**Output:** [[1,2,6],[1,3,5],[2,3,4]]
**Explanation:**
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

'''
def combinationSum3(k, n):
    ans, cur = [],[]
    def backtrack(cur, i, sum):
        if len(cur) == k and sum == n:
            # notice this clever sort here so that
            # we can check if it is already there
            # cur.sort()
            ans.append(cur[:])
            return
        if sum > n or len(cur) > k:
            return 
        for i in range(i,10):
            # we can only use numbers 1-9
            # if num not on cur
            #if i not in cur:
            cur.append(i)
            backtrack(cur, i+1, sum + i)
            cur.pop()
    backtrack(cur, 1, 0)
    return ans

print(combinationSum3(3, 7)) # [[1,2,4]]
print(combinationSum3(3, 9)) # [[1,2,6],[1,3,5],[2,3,4]]
print(combinationSum3(4, 1)) # []
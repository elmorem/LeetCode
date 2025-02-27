'''
Given an array `nums` of distinct integers, return all the possible 

permutations

. You can return the answer in **any order**.
- the number of combinations possible is n! where n is len(nums)

**Example 1:**

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


def permute(lst):
    n = len(lst)
    sol, ans = [],[]
    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return
        for j in range(n):
            if lst[j] not in sol:
                sol.append(lst[j])
                backtrack()
                sol.pop()
    backtrack()
    return ans
print(permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print("-------------")
print(permute([1,2,3,4])) # [[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,[1],2,[4],1,[2],3,[4],2,[1],3,[4],[2],1,[3],4,[2],1,[3],4,[2],[1],3,[4],2,[1],3,[4],2,[1],3,[4],2,[1],3,[4],[2],[1],3,[4],2,[1],3,[4],[2],[1],3,[4],[2],[1],3,[4]]]
print("-------------")
print(permute([1,2,3,4,5])) # [[1,2,3,4,5],[1,2,3,5,4],[1,2,4,3,5],[1,2,4,5,3],[1,2,5,3,4],[1,2,5,4,3],[1,3,[2],4,[5],1,[2],3,[5],4,[2],1,[3],5,[4],2,[1],3,[5],4,[2],1,[3],5,[4],[2],1,[3],5,[4],[2],[1],3,[5],4,[2],[1],3,[5],[4],[2],[1],3,[5]]]

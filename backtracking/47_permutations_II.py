'''
Given a collection of numbers, `nums`, that might contain duplicates, return _all possible unique permutations **in any order**._

**Example 1:**

**Input:** nums = [1,1,2]
**Output:**
[[1,1,2],
 [1,2,1],
 [2,1,1]]
INTUiTION:  we are going to deal with the duplicate numbers in the array by using a Counter object and iterating through that one instad of the simply array 
'''
from collections import Counter
def permuteUnique(nums):
    ans, sol = [], []
    count = Counter(nums)
    def backtrack():
        # base case
        # we don't need to pass in i because we can just check the length of the sol
        # and the count of the numbers
        if len(sol) == len(nums):
            ans.append(sol[:])
            return
        for n in count:
            if count[n]>0:  
                # this is the key condition.  it ensures that we only add accordign to its 
                # frequency in the original array
                sol.append(n)
                count[n] -=1  # decrement the count 
                backtrack() # recursive call
                count[n] +=1 
                # increment the count 
                # 
                sol.pop() # then remove it
    backtrack()
    return ans

print(permuteUnique([1,1,2])) # [[1,1,2],[1,2,1],[2,1,1]]
print("-------------")
print(permuteUnique([1,1,2,2])) # [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
print("-------------")
print(permuteUnique([1,1,2,2,3])) # [[1,1,2,2,3],[1,1,2,3,2],[1,1,3,2,2],[1,2,1,2,3],[1,2,1,3,2],[1,2,2,1,3],[1,2,2,3,1],[1,2,
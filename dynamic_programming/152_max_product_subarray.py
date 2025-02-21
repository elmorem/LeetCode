'''
- a key here is that we should calculate both the max product subarray and the min product subarray for each one 
- Given an integer array `nums`, find a subarray that has the largest product, and return _the product_.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Example 1:**

**Input:** nums = [2,3,-2,4]
**Output:** 6
**Explanation:** [2,3] has the largest product 6.
'''

def maxProduct(nums):
    result = max(nums) # starts us off with the max number in nums
    curMin, curMax = 1, 1
    for n in nums:
        tmp = curMax*n # store curMax*n so we can use it to update curMin
        curMax = max(n, curMax*n, curMin*n)
        curMin = min(n, tmp, curMin*n)
        result = max(result, curMax) #  update result if curMax is greater
    return result
print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([-2,0,-1])) # 0
print(maxProduct([-2])) # -2
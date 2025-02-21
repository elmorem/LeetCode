'''
Given an integer array `nums`, return `true` _if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or_ `false` _otherwise_.

**Example 1:**

**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].
create a set that is all possible sums of each subset.  check if any of them is half the total sum
'''
def canPartition(nums):
    target = sum(nums)/2
    if sum(nums) % 2:
        return False
    dp = {0}
    for n in nums:
        next_dp = set()
        for s in dp:
            next_dp.add(s + n)
            next_dp.add(s)
        dp = next_dp
    return target in dp


print(canPartition([1,5,11,5])) # True
print(canPartition([1,2,3,5])) # False
print(canPartition([1,2,3,4])) # True
print(canPartition([1,2,3,5,6])) # False
print(canPartition([1,2,3,4,5])) # False
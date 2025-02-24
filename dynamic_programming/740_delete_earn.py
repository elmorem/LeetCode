'''
You are given an integer array `nums`. You want to maximize the number of points you get by performing the following operation any number of times:

- Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterwards, you must delete **every** element equal to `nums[i] - 1` and **every** element equal to `nums[i] + 1`.

Return _the **maximum number of points** you can earn by applying the above operation some number of times_.

**Example 1:**

**Input:** nums = [3,4,2]
**Output:** 6
**Explanation:** You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
**Input:** nums = [2,2,3,3,3,4]
**Output:** 9
**Explanation:** You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        c = Counter(nums)
        dp = [1 for x in range(len(c))] 
        # basically instead of dp since we only need the 2 values before the current one
        # we are just going to use earn1 and earn2 as placeholders for those values as we 
        #move through the array
        earn1, earn2 = 0,0
        nums = list(c.keys())
        for i in range(len(nums)):
            curEarn = nums[i]*c[nums[i]]
            if i > 0 and nums[i] == nums[i-1]+1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2
print(Solution().deleteAndEarn([3,4,2])) # 6
print(Solution().deleteAndEarn([2,2,3,3,3,4])) # 9
print(Solution().deleteAndEarn([1,2,3,4,5])) # 15
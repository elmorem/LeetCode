from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        smallest = float("inf")
        total = 0
        for r in range(n):
            total += nums[r]
            while total >= target:
                w = (r-l)+1
                smallest = min(smallest, w)
                total -= nums[l]
                l+=1
        return smallest if smallest < float("inf") else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # Expected output: 2
    print(solution.minSubArrayLen(4, [1,4,4]))        # Expected output: 1
    print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # Expected output: 0

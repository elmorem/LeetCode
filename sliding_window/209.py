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
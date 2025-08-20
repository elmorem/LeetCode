class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = defaultdict(int)
        nums.sort()
        for i in range(n):
            lo = i+1
            hi = n-1
            while lo < hi:
                summ = nums[i]+nums[lo]+nums[hi]
                if summ == 0:
                    answer[(nums[i], nums[lo], nums[hi])]
                    lo +=1
                    hi -=1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo +=1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -=1
                elif summ < 0:
                    lo +=1
                else:
                    hi -=1
        return list(answer.keys())
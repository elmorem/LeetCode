from collections import defaultdict
from typing import List
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
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))  # Expected output: [[-1,-1,2],[-1,0,1]]
    print(solution.threeSum([]))                 # Expected output: []
    print(solution.threeSum([0]))                # Expected output: []
    print(solution.threeSum([1,7,-6,220,-4320]))          # Expected output: []
    print(solution.threeSum([0,0,0,0]))          # Expected output: [[0,0,0]]       
    print(solution.threeSum([-2,0,1,1,2]))       # Expected output: [[-2,1,1],[-2,0,2]]
    print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))  # Expected output: [[-4,-2,6],[-4,0,4],[-4
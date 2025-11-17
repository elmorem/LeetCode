
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_sum = nums[0]+nums[1]+nums[2]
        best_diff = abs(best_sum - target)
        for i in range(n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j <k:
                s = nums[i]+ nums[j]+ nums[k]
                diff = s-target
                if abs(diff) < best_diff:
                    best_diff =  abs(diff)
                    best_sum = s
                if diff == 0:
                    return target
                elif diff <0:
                    j +=1
                else:
                    k-=1
        return best_sum
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [-1,2,1,-4]
    target1 = 1
    print(sol.threeSumClosest(nums1, target1))  # Expected output: 2

    nums2 = [0,0,0]
    target2 = 1
    print(sol.threeSumClosest(nums2, target2))  # Expected output: 0
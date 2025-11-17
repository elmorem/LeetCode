from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, t):
            drops= len(nums) - t
            stack = []
            for x in nums:
                while drops and stack and stack[-1] <x:
                    stack.pop()
                    drops -=1
                stack.append(x)
            return stack[:t]
        def greater(a,i,b,j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i+=1
                j+=1
            return j == len(b) or (i < len(a) and a[i] > b[j])
        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if greater(a,i,b,j):
                    res.append(a[i])
                    i +=1
                else:
                    res.append(b[j])
                    j +=1
            return res
        n1, n2 = len(nums1), len(nums2)
        best = []
        start = max(0,k-n2)
        end = min(k, n1)
        for i in range(start, end +1):
            
            cand = merge(pick(nums1, i), pick(nums2, k-i))
            if not best or greater(cand, 0,best,0):
                best = cand
        return best
if __name__ == "__main__":
    sol = Solution()
    nums1 = [3,4,6,5]
    nums2 = [9,1,2,5,8,3]
    k = 5
    print(sol.maxNumber(nums1, nums2, k))  # Expected output: [9,8,6,5,3]

    nums1 = [6,7]
    nums2 = [6,0,4]
    k = 5
    print(sol.maxNumber(nums1, nums2, k))  # Expected output: [6,7,6,0,4]

    nums1 = [3,9]
    nums2 = [8,9]
    k = 3
    print(sol.maxNumber(nums1, nums2, k))  # Expected output: [9,8,9]   
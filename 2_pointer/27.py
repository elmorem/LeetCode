class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i] == val:
                print(f"nums[i]={nums[i]}")
                nums[i] = nums[n-1]
                print(f"nums[n-1]={nums[n-1]}")
                n -= 1
            else:
                print(f"nums[i] other num={nums[i]}")
                i += 1
        print(n)
        return n

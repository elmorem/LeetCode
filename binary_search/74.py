class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        l = 0
        r = t-1
        while l <= r:
            mid = (l+r)//2
            print(f"m={mid}")
            i = mid // n
            print(f"i={i}")
            j = mid % n
            print(f"j={j}")
            mid_num = matrix[i][j]
            if target == mid_num:
                return True
            if target < mid_num:
                r = mid-1
            else:
                l = mid +1
        return False
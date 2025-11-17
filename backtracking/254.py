from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def dfs(curr, start, path):
            i =start
            while i *i <= curr:
                if curr % i ==0:
                    res.append(path + [i, curr // i])
                    dfs(curr // i,i,path+[i])
                i +=1
        dfs(n, 2, [])
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.getFactors(12))  # Expected output: [[2,6],[2,2,3],[3,4]]
    print(solution.getFactors(15))  # Expected output: [[3,5]]
    print(solution.getFactors(16))  # Expected output: [[2,8],[2,2,4],[2,2,2,2],[4,4]]
    print(solution.getFactors(37))  # Expected output: []
    print(solution.getFactors(100)) # Expected output: [[2,50],[2,2,25],[2,5,10],[4,25],[5,20],[10,10]]
    print(12//2)
    print(11//2)
    print(11/2)
    print(12%2)
    print(11%2)
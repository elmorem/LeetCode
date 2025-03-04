'''
You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent** **substrings** is equal to `1`.

- For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.
- Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` _if it is possible to split_ `s`​​​​​​ _as described above__, or_ `false` _otherwise._

A **substring** is a contiguous sequence of characters in a string.

**Example 1:**

**Input:** s = "1234"
**Output:** false
**Explanation:** There is no valid way to split s.

**Example 2:**

**Input:** s = "050043"
**Output:** true
**Explanation:** s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.


> [!NOTE] Algo Summary
> 1. Initialize
> 2. Recursive backtrack returns nothing
> 	1. 2 base cases 1. if the difference between 2 consecutive valoues in part do not differ by 1. ans 2. if i == n
> 	2. Otherwise we just do the basic backtrack
> 3. if there is any value in ans we return true flase otherwise

'''

class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        part = []
        n = len(s)
        def backtrack(i):
            if len(part) >=2 and int(part[-2])- int(part[-1]) !=1:
                #print(f"{int(part[-2]) = }")
                #print(f"{int(part[-1]) = }")
                return
            elif i == n:
                if len(part[0]) == n:
                    return
                else:
                    #print(f" {len(part) = } {n = }")
                    #print(f"appending ans {part = } {ans = } ")
                    ans.append(part[:])
                    return
            for j in range(i, n):
                part.append(s[i:j+1])
                #print(f"part at backtrack {part = }")
                backtrack(j+1)
                part.pop()
        backtrack(0)
        #print(f"{ans = }")
        return False if not ans else True
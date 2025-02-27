'''
-IMPORTANT:  this one shows a complicated way to do the recursion

-intution:  the idea here is:  where are we going to place the 3 periods
A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

- For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return _all possible valid IP addresses that can be formed by inserting dots into_ `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

**Example 1:**

**Input:** s = "25525511135"
**Output:** ["255.255.11.135","255.255.111.35"]

'''
def restoreIpAddresses(s):
    ans = []
    if len(s) > 12:
        return []
    def backtrack(i, dots, curIP):
        if dots == 4 and i == len(s):
            ans.append(curIP[:-1])
            return
        if dots > 4:
            return
        for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                backtrack(j+1, dots+1, curIP + s[i:j+1] + '.') # j+1 because we are moving on to the next set of numbers

    backtrack(0, dots=0, curIP="")
    return ans

print(restoreIpAddresses("25525511135")) # ['255.255.11.135', '255.255.111.35']
print(restoreIpAddresses("0000")) # ['0.0.0.0']
print(restoreIpAddresses("1922724")) # ['1.9.227.24', '1.92.27.24', '19.2.27.24', '19.22.7.24', '19.22.72.4', '19.227.2.4', '192.2.7.24', '192.2.72.4', '192.27.2.4']

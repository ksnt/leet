class Solution:
    def countAndSay(self, n):
        res = "1"
        for _ in range(n-1):
            res = self.solve(res)
        return res

    def solve(self,n):
        count = 1
        i = 0
        res = ""
        while  i < len(n) -1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res

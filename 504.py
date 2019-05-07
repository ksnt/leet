class Solution:
    def convertToBase7(self,num: int) -> str:
        flag = 0
        res = ""
        if num == 0:
            return "0"
        if num < 0:
            num = -num
            flag = 1 # negative flag
        if num > 0:
            while (num > 0):
                res = str(num % 7) + res
                num = num //  7
        if flag == 1: # negative flag
            res = "-" + res
        return res
class Solution:
    def myAtoi(self,str):
        """
        :type str: str
        :rtype: int
        """
        res = ""
        str = str.strip(" ")
        #str = str.strip("+")
        if str == "": return 0
        if str[0] == "+" or str[0] == "-":
            sign = 1
        else:
            sign = 0
        for s in str[sign:]:
            if s.isdigit():
                res = res+s
            else:
                break
        #print(res)
        if res == "":
            return 0
        else:
            if sign == 1:
                res = str[0] + res
            else:
                 pass
        if "." in res:
            res = float(res)
        else:
            res = int(res)
        if res < -2147483648:
            return -2147483648
        elif res >= 2147483648:
            return 2147483647
        else:
            return res
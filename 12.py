def one(n):
    if n == 1:
        return "I"
    elif n == 2:
        return "II"
    elif n == 3:
        return "III"
    elif n == 4:
        return "IV"
    elif n == 5:
        return "V"
    elif n == 6:
        return "VI"
    elif n == 7:
        return "VII"
    elif n == 8:
        return "VIII"
    elif n == 9:
        return "IX"
    elif n == 0:
        return ""

 
def ten(n):
    if n == 1:
        return "X"
    elif n == 2:
        return "XX"
    elif n == 3:
        return "XXX"
    elif n == 4:
        return "XL"
    elif n == 5:
        return "L"
    elif n == 6:
        return "LX"
    elif n == 7:
        return "LXX"
    elif n == 8:
        return "LXXX"
    elif n == 9:
        return "XC"
    elif n == 0:
        return ""


def hundred(n):
    if n == 1:
        return "C"
    elif n == 2:
        return "CC"
    elif n == 3:
        return "CCC"
    elif n == 4:
        return "CD"
    elif n == 5:
        return "D"
    elif n == 6:
        return "DC"
    elif n == 7:
        return "DCC"
    elif n == 8:
        return "DCCC"
    elif n == 9:
        return "CM"
    elif n == 0:
        return ""


def thousand(n):
    if n == 1:
        return "M"
    elif n == 2:
        return "MM"
    elif n == 3:
        return "MMM"
    elif n == 0:
        return ""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = num // 1000
        num = num % 1000
        b = num // 100
        num = num % 100
        c = num // 10
        d = num % 10
        return (thousand(a)+hundred(b)+ten(c)+one(d))
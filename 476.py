class Solution:
    def findComplement(self,num):
        """
        :type num: int
        :rtype: int
        """
        import functools
        binary = bin(num)[2:]
        bin_list = [b for b in binary]
        for i,b in enumerate(bin_list):
            if b == "0":
                bin_list[i] = "1"
            else:
                bin_list[i] = "0"
        return int(functools.reduce(lambda x,y: x+y,bin_list),2)

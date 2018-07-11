class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        J_list = list(J)
        for s in S:
            if s in J_list:
                total = total + 1
        return total
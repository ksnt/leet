class Solution:
    def rotateString(self,A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        for k in range(len(B)):
        	if B[-k:] + B[:-k] == A:
        		return True
        return False
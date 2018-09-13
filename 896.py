class Solution:
    def isMonotonic(self,A):
        """
        :type A: List[int]
        :rtype: bool
        """
        status = True
        # for monotnic decrease
        for i in range(len(A)-1):
        	if A[i] >= A[i+1]:
        		pass
        	else:
        		status = False
        		break
        if status == True: return status
        # for monotnic increasing
        for i in range(len(A)-1):
        	if A[i] <= A[i+1]:
        		pass
        	else:
        		status = False
        		return status
        return True
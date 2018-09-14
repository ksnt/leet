class Solution:
    def fairCandySwap(self,A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(A)):
            for j in range(len(B)):
                #exchange items
                tmp = A[i]
                A[i] = B[j]
                B[j] = tmp
                if sum(A) == sum(B):
                    result.append(B[j])
                    result.append(A[i])
                    return result
                else:
                    tmp2 = A[i]
                    A[i] = B[j]
                    B[j] = tmp2
        # now it is assumed that there is atleat one answer
        # therefore, the code below will never be executed
        return "finished" 
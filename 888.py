class Solution:
    def fairCandySwap(self,A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff  = sum(A) - sum(B)
        A = set(A)
        B = set(B)
        for a in A:
                # in general we should not use this way:
                #  deivide diff by 2 and meke it integer type
                target = int(a - diff/2)
                if target in B:
                    return [a,target]
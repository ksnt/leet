class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = [i for i in A if i%2==0 ]
        odd = [j for j in A if j%2==1]
        res = []
        for i in range(len(A)):
            if i%2==0:
                res.append(even.pop())
            else:
                res.append(odd.pop())
        return res
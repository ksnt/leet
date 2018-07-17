class Solution:
    def isHappy(self,n):
        """
        :type n: int
        :rtype: bool
        """
        store = set()
        while(n!=1):
            n = sum([int(x) * int(x) for x in str(n)])
            if n in store:
                return False
            else:
                store.add(n)
        return True
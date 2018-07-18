# Time Limit Exceeded
# Inefficient
class Solution:
    def findErrorNums(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = 0
        store = []
        res = []
        for n in nums:
            if n not in store:
                store.append(n)
            else:
                res.append(n)
        #print(store)
        #print(res)
        res.append((set(x for x in range(1,len(nums)+1)) - set(store)).pop())
        return res
#Solution using DP
class Solution:
    def rob(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = [0,0]
        for i in range(2,len(nums)+2):
            store.append(max(store[i-2]+nums[i-2],store[i-1]))
        #print(store)
        return store[-1]
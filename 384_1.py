import numpy as np
import copy
# All test cannot be passed...
class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store = nums
        self.current = copy.deepcopy(nums)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.current = self.store
        return self.current


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random_n = np.random.randint(len(self.current))
        random_m = np.random.randint(len(self.current))
        tmp = self.current[random_n]
        self.current[random_n] = self.current[random_m]
        self.current[random_m] = tmp
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
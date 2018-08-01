# TLE solution
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        #import statistics
        self.nums = []   
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.nums.append(num)
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.nums) == 0:
            return None
        else:
            length = len(self.nums)
        nums_sorted = sorted(self.nums)
        if len(self.nums) % 2 == 1:
            return float(nums_sorted[int(length/2)])
        else:
            return  float((nums_sorted[int(length/2) - 1] + nums_sorted[int(length/2)]) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# obj.findMedian()
# obj.addNum(3)
# obj.findMedian()
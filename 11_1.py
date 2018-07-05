# 1.Brute Force 
# Time complexity: O(n^2)
def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = []
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                h = min(height[i],height[j])
                l = j - i
                res.append(h*l)
        return (max(res))
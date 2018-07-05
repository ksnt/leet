# 2.Two Pointer Approach
# I do not know why this can be a solution to search for all possible patters without proof...
def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_container = 0
        i = 0
        j = len(height) -1
        while i < j:
            current_container = (j-i) * min(height[i],height[j])
            max_container = max(max_container,current_container)
            if height[i] < height[j]: i += 1
            else: j -= 1
        return max_container
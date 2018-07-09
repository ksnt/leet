# Efficient version
# calculas complexity: O(n)?
class Solution:
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        current_value = max_value = ''
        for s_i in s:
            current_value = current_value + s_i if s_i not in current_value else current_value[current_value.find(s_i) + 1: ] + s_i
            max_value = max_value if len(max_value) > len(current_value) else current_value
        return len(max_value)
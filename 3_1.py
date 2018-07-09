# Inefficient version
# calculas complexity: O(n^2)
# space complexity: O(n^2)
# Note: "append" method would be slow

class Solution:
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        result = []
        for i in range(len(s)):
            result_i = s[i] # string
            tmp = [s[i]]    # list
            for j in range(i+1,len(s)):
                if s[j] not in tmp:
                    result_i = result_i + s[j]
                    tmp.append(s[j])
                else:
                    result.append(result_i)
                    break
            result.append(result_i)
        #print(result)
        return max(list(map(lambda x: len(x),result)))
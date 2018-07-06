class Solution:
   def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        count_I = 0
        count_X = 0
        count_C = 0
        for i in s:
            if i == 'I':
                count_I += 1
                sum += 1
            elif i == 'V':
                if count_I == 1:
                    sum += 3
                else:
                    sum += 5
            elif i == 'X':
                count_X += 1
                if count_I == 1:
                    sum += 8
                else:
                    sum += 10
            elif i == 'L':
                if count_X == 1:
                    sum += 30
                else:
                    sum += 50
            elif i == 'C':
                count_C += 1
                if count_X == 1:
                    sum += 80
                else:
                    sum += 100
            elif i == 'D':
                if count_C == 1:
                    sum += 300
                else:
                    sum += 500
            elif i == 'M':
                if count_C == 1:
                    sum += 800
                else:
                    sum += 1000
        return sum
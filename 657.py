class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sum1 = [] # y-axis
        sum2 = [] # x-axis
        for m in moves:
            if m == "U":
                sum1.append(1)
            elif m == "D":
                sum1.append(-1)
            elif m == "L":
                sum2.append(-1)
            elif m == "R":
                sum2.append(1)
            else:
                print("you should think of this case!")
        if sum(sum1) == 0 and sum(sum2) == 0:
            return True
        else:
            return False
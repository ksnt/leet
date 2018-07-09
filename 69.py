# Babylonian method
# reference: https://cpplover.blogspot.com/2010/11/blog-post_20.html
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        s = x / 2
        last_x = 0
        while (s != last_x):
            last_x = s
            s = (s + x / s) / 2
        return int(s)

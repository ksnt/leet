class Solution:
    def hammingDistance(self,x: 'int', y: 'int') -> 'int':
        res = 0
        hum_x = bin(x)[2:]
        hum_y = bin(y)[2:]
        if x > y:
            length = len(hum_x)
            hum_y = hum_y.zfill(length)
        else:
            length = len(hum_y)
            hum_x = hum_x.zfill(length)
        #print(hum_y)
        for i in range(len(hum_x)):
            res = res + abs(int(hum_x[i]) - int(hum_y[i]))
        return res
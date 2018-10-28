class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n==2: return 0
        max = int(n)
        flags = [True for _ in range(max)]
        flags[0] = False
        flags[1] = False
        prime = 2
        
        while prime <= max:
            #print(flags)
            # Erase all numbers which is multiple of remaining primes
            self.crossOff(flags,prime)
        
            # Find a next prime which flag is true 
            prime = self.getNextPrime(flags,prime)
            if prime >= len(flags):
                break
        return len([i for i,v in enumerate(flags) if v == True])
    
    def crossOff(self,flags, prime):
        start = prime * prime
        for i in range(start,len(flags),prime):
            flags[i] = False
            
    def getNextPrime(self,flags,prime):
        next = prime + 1
        while next < len(flags) and (not flags[next]):
            next = next  + 1
        return next
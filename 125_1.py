class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = re.sub(re.compile("[!-/:-@[-`{-~\s]"), '', s).lower()
        if len(a) % 2 == 0:
            return a[0:len(a)//2] == a[::-1][0:len(a)//2]
        else:
            return a[0:len(a)//2] == a[::-1][0:len(a)//2]
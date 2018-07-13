class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = re.sub(re.compile("[!-/:-@[-`{-~\s]"), '', s).lower()
        return a[0:len(a)//2] == a[::-1][0:len(a)//2]
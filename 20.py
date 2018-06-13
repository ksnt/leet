class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_pars = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                left_pars.append(i)
            elif i == ')':
                if len(left_pars) == 0: return False
                elif left_pars.pop() == '(': pass
                else: return False
            elif i == '}':
                if len(left_pars) == 0: return False
                elif left_pars.pop() == '{': pass
                else: return False
            elif i == ']':
                if len(left_pars) == 0: return False
                elif left_pars.pop() == '[': pass
                else: return False
        if len(left_pars) == 0: return True
        else: return False


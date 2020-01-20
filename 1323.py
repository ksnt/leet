class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        result = [num_str]
        for i,s in enumerate(num_str):
            if s == "6":
                res = num_str[:i] + "9" + num_str[i+1:]
                result.append(res)
            else:
                res = num_str[:i] + "6" + num_str[i+1:]
                result.append(res)
        return max(list(map(int,result)))
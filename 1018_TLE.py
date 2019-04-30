import functools

def prefixesDivBy5(A: List[int]) -> List[bool]:
    result = []
    for i in range(1,len(A)+1):
        result.append(int(functools.reduce(lambda x, y : x + y, list(map(str,A[:i]))),2) % 5 == 0)
    return result
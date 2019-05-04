# In this approach, I did not think of duplicated characters...
def commonChars(A: List[str]) -> List[str]:
    res = []
    base = A[0]
    residuals = A[1:]
    for i in range(len(base)):
       for j in range(1,len(residuals)+1):
            #print(i)
            print(j)
            if not (base[i] in A[j]):
                print("hoge")
                break
            if j == len(residuals) and base[i] in A[j]:
                print("pom")
                res.append(base[i])
    return res
L=[0,2,3,5,9]
M=L[0]
n=len(L)
for i in range(0, n):
    if L[i]>M:
        M=L[i]
print(M)
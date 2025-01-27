def func_divSucc():
    return 0

a=int(input("val 1"))
b=int(input("val 2"))
d=1
tmpA=a
tmpB=b

while d > 0:
    if a-b >= 0:
        d=a-b
    else:
        a=d
        b=tmpB
        d = a - b
    tmpA=a
    tmpB=b
    a=b
    b=d
print(a)
#Convert Double to Bin
a=eval(input("Saisissez un nombre à virgule : "))
a=a*2
a1=int(a)
a=(a-a1)*2
a2=int(a)
a=(a-a2)*2
a3=int(a)
a=(a-a3)*2
a4=int(a)
print(str(a1)+str(a2)+str(a3)+str(a4))
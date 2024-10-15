#Convert Octet Number to Bin
a=int(input("Saisissez un nombre octet : "))
q1=a//2
r1=a%2
q2=q1//2
r2=q1%2
q3=q2//2
r3=q2%2
q4=q3//2
r4=q3%2
q5=q4//2
r5=q4%2
q6=q5//2
r6=q5%2
q7=q6//2
r7=q6%2
q8=q7//2
r8=q7%2
print(str(r8)+str(r7)+str(r6)+str(r5)+str(r4)+str(r3)+str(r2)+str(r1))
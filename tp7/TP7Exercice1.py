#III Ex 1
phrase=input("Saisissez une phrase : ")
reverseStr=""
for i in range(len(phrase)-1, -1, -1):
    reverseStr=reverseStr+phrase[i]
print(reverseStr)
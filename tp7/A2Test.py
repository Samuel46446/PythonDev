import string
from array import array

message=input("Saisissez votre message : ")
n=len(message)
i=0

alphabet_min = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
alphabet_maj = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

occu=[0]*26

while i < n:
    for k in range(0, len(alphabet_maj)):
        if message[i] == alphabet_min[k] or message[i] == alphabet_maj[k]:
            occu[k]=occu[k]+1
    i=i+1
print(message)
print(occu)

strMin="["
strMax="["
for o in range(0, 25):
    strMin=strMin+alphabet_min[o]+", "
strMin=strMin+alphabet_min[25]+"]"
print(strMin)

for o in range(0, 25):
    strMax=strMax+alphabet_maj[o]+", "
strMax=strMax+alphabet_min[25]+"]"
print(strMax)
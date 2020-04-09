msg1 = input(" Enter the string \n")

uc = 0
lc = 0

for i in range(len(msg1)):
    if(msg1[i].isupper()):
        uc = uc+1
    elif(msg1[i].islower()):
        lc = lc+1

print("The message is "+msg1)
print("The number of uppercase letters ",uc)
print("The number of lowercase letters ",lc)
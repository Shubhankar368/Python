str=input("enter the string: ")
upper=0
lower=0
for i in range(0,len(str)) :
    if str[i].islower()==True:
        lower=lower+1
    else:
        upper=upper+1
print("no of lower case letters in string: ",lower)
print("no of uppercase letters in string: ",upper)
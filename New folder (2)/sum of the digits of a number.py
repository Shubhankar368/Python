#to find the sum of the digits of a number
N1=int(input("enter the number: "))
num=0
while N1>0:
	number=N1%10
	N1=N1//10
	num=num+number
print("the sum of the numbers is: ",num)
print("thank you for using python")
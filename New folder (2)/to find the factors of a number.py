#to find the factors of a number
N1=int(input("enter the number to find its factor: "))
print(1,end=" ")
fact=2
while fact<=N1/2:
	if N1%fact==0:
		print(fact,end=" ")
	fact=fact+1
print(N1,"are the factors of the number",end=" ")

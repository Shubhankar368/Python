N1=int(input("enter first number: "))
N2=int(input("enter second number: "))
for a in range(N1,N2):
	if a%2==0:
		print(a, "its an even number")
	else:
		print(a, "its an odd number")
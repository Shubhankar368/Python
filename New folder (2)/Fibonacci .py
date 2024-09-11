i=int(input("Enter the limit: "))
x=0
y=0
z=1
print("Fibonacci series \n")
print(x,y,end=" ")
while (z<=i):
	print(z,end=" ")
	x=y
	y=z
	z=x+y
	
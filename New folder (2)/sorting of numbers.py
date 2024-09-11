# a program to sort 3 numbers
N1=float(input("enter first number: "))
N2=float(input("enter second number: "))
N3=float(input("enter third number: "))
x=max(N1,N2,N3)
z=min(N1,N2,N3)
w=(N1+N2+N3)-z-x
print("the numbers are: " ,x,w,z)
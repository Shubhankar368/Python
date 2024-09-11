#to find the smallest number out of three numbers 
N1=int(input("enter first number: "))
N2=int(input("enter second number: "))
N3=int(input("enter third number: "))
if N1<N2 or N1<N3:
	print(N1,"is the smallest no out of",N1,",",N2,"and",N3)
elif N2<N1 or N2<N3:
	print(N2,"is the smallest no out of",N1,",",N2,"and",N3)
elif N3<N1 or N3<N2:
	print(N3,"is smallest no out of",N1,",",N2,"and",N3)
else:
	print("invalid data")
print("Thank you for using my program \n Have a nice day!")
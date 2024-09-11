N1=int(input("enter total bill: "))
if N1>=20000:
	x=N1-15/100*N1
	print("you have to pay:$",x)
elif N1>=15000:
	x=N1-10/100*N1
	print("you have to pay:$",x)
elif  N1>=10000:
	x=N1-5/100*N1
	print("you have to pay:$",x)
else:
	print("sorry no discount you have to pay:$",N1)
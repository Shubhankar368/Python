#to find the marks of students
N1=int(input("enter the marks of maths: "))
N2=int(input("enter the marks of physics hundred: "))
N3=int(input("enter the marks of chemistry: "))
N4=int(input("enter the marks of computer science: "))
N5=int(input("enter the marks of painting: "))
X=N1+N2+N3+N4+N5
print("total is: ",X)
percentage=X/500*100
print("percentage is: ",percentage)
if percentage>=90:
	print("your grade is A \n well done!")
elif percentage>85 and percentage<90:
	print("your grade is B \n almost perfect")
elif percentage>75 and percentage<85:
	print("your grade is C \n can do better")
else:
	print("your grade is D \n need more practice")
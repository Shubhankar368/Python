#to find the marks of students
N1=int(input("enter the marks of maths: "))
if N1>100:
	print("please enter the correct marks")
N2=int(input("enter the marks of physics hundred: "))
if N2>100:
	print("please enter the correct marks")
N3=int(input("enter the marks of chemistry: "))
if N3>100:
	print("please enter the correct marks")
N4=int(input("enter the marks of computer science: "))
if N4>100:
	print("please enter the correct marks")
N5=int(input("enter the marks of painting: "))
if N5>100:
	print("please enter the correct marks")
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
'''2. Write a program to check whether a triangle is valid or not if sides are given.
'''


print("Enter sides of a TRIANGLE")
a=int(input())
b=int(input())
c=int(input())

if (a+b)>c and (b+c)>a and (c+a)>b:
	print("The TRINAGLE is valid")
else:
	print("The TRIANGLE is invalid")

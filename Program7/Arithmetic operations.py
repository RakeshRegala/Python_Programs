def add(a,b):
	return a+b
	
def subtract(a,b):
	return a-b
	
def multiply(a,b):
	return a*b
	
def divide(a,b):
	if b == 0:
		return "Error!Division by zero"
	else:
		return a/b
	
print("1.Add	2.Subtract	3.Multiply 	4.Divide")

ch=int(input("Enter choice:"))
print("Enter 1st number:")
a=int(input())
b=int(input("Enter 2nd number:"))

if ch == 1:
	print("Addition of",a,"and",b,"is:",add(a,b))
elif ch == 2:
	print("Subtraction of",a,"and",b,"is:",subtract(a,b))
elif ch == 3:
	print("Multiplication of ",a,"and",b,"is:",multiply(a,b))
elif ch == 4:
	print("Division of",a,"and",b,"is:",divide(a,b))
	

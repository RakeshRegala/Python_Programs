#finding the factorial of a number

n=int(input("Enter a number: "))
p=1
for i in range(1,n+1):
	p=p*i
print(f"The factorial of {n} is {p}")

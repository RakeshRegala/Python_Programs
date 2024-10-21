def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a
	
a=int(input("Enter 2 numbers:"))
b=int(input())

print("GCD is:",gcd(a,b))\

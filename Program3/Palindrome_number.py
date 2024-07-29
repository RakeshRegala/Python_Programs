# Palindrome 

n=int(input("Enter a number: "))
temp = n
rev=0
while n>0:
	rem=n%10
	n=n//10
	rev=rev*10+rem
if rev == temp:
	print(f"{temp} is a palindrome number")
else:
	print(f"{temp} is not palindrome number")

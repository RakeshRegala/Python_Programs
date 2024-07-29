#Finding wheather a number is armstrong number or not

n=int(input("Enter a number: "))
k=n
sum=0
while n!=0:
	r=n%10
	n=n//10
	sum=sum+r**3
if k==sum:
	print(f"{k} is an armstrong number")
else:
	print(f"{k} is not an armstrong number")
	

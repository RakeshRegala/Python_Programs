n=int(input("Enter a number: "))
sum=0
i=1
f=1
while i<=n:
	f=1
	for j in range(1,i+1):
		f=f*j
	sum=sum+i/f
	i=i+1
print(f"The sum of series for {n} is {sum}")

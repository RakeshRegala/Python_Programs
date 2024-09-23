l=[]

n=int(input("Enter no of elements"))
print("Enter",n,"elements")

for i in range(n):
	ele=int(input())
	l.append(ele)
	
print(f"Sum of {l}: ",sum(l))
print(f"Average of {l}: ",sum(l)/len(l))

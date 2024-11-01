def reverse(list):
	rev=[]
	for i in range(len(list)):
		rev.append(list.pop())
		
	return rev
	

list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
print(f"List before reversing: {list}")
print(f"List after reversing : {reverse(list)}")

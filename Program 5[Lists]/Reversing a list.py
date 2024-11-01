list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)

print(f"List before reversing{list}:")

print("List after reversing")
print(list[::-1])

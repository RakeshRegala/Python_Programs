list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
    
list[0],list[-1]=list[-1],list[0]

print("List after interchanging first and last elements:",list)

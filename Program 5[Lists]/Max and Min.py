list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)

print("Max no in list is at index:",list.index(max(list)))
print("Min no in list is at index:",list.index(min(list)))

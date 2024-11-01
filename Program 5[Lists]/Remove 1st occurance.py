
list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
    
r=int(input("Enter element to be removed "))
for i in list:
    if r==i:
        list.remove(i)
        break
print(list)
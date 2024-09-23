list=[]
even=[]
odd=[]


n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
    
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even-",even)
print("Odd-",odd)

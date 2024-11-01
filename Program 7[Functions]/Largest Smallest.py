def findMaxMin(list):
	big = max(list)
	small = min(list)
	return big,small


list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
    
largest,smallest = findMaxMin(list)
print("List is: ",list)
print("Largest number is:",largest)
print("Smallest number is:",smallest)

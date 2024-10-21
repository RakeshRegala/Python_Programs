def findSecondMax(list):
	big1 = max(list)
	list.remove(big1)
	big2 = max(list)
	return big2


list=[]

n=int(input("Enter the number of elements: "))
print("Enter",n,"elements")

for i in range(n):
    ele=int(input())
    list.append(ele)
    
largest=findSecondMax(list)
print("List is: ",list)
print("Second Largest number is:",largest)

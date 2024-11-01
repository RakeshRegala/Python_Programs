str=input("Enter a string: ")
vowels="aeiouAEIOU"
count = 0
for i in str:
    if i in vowels:
        count = count+1
print(f"The no of vowels in {str} is:",count)

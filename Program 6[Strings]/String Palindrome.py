str=input("Enter a String: ")
rev=""
for i in str:
    rev = i+rev

if rev == str:
    print("Yes!The given string",str,"is Palindrome")
else:
    print("The String",str,"is not Palindrome")

str=input("Enter a string: ")
words=str.split()
even_list=[test for test in words if len(test)%2 == 0]
print("Even length words are:",even_list)

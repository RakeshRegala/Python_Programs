a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a>b and a>c:
    print("Biggest number is",a)
elif b>a and b>c:
    print("Biggest number is",b)
else:
    print("Biggest number is",c)

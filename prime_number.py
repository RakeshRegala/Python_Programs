#printing prime numbers in an interval


ll=int(input("ENTER LOWER LIMIT"))
ul=int(input("ENTER UPPER LIMIT"))
f=0
print("The prime numbers b/w",ll,"and",ul)
while ll<=ul:                            #control b/w limits
    f=0
    x=1
    for x in range(1,ll+1,1):               
        if ll % x == 0:             #checking factors
            f=f+1
    if f == 2:
        print(ll)
    ll=ll+1
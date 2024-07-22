#FIND THE SPEED FOR GIVEN DISTANCE(km) AND TIME(min)

distance=int(input("Enter the DISTANCE in km: "))              #input in kilometers
time=int(input("Enter the Time: "))         #input time in minutes
time=time/60                #converting time from minutes to hours
speed=distance/time
print("SPEED(km/hr): ",speed)

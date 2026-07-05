#the error code 

# fahrenheit = input("Enter temp in F:")
# celsius = (fahrenheit - 32) * 5/9
# print("Temperature in C:" celsius)

#debugged code
try:
    fahrenheit = int(input("Enter temp in F:"))
    celsius = (fahrenheit -32) * 5/9
    print("Temperatur in C:", celsius)

except ValueError:
    print("Invalid Input")

help ValueError

#output 
# #the error code 

# fahrenheit = input("Enter temp in F:")
# celsius = (fahrenheit - 32) * 5/9
# print("Temperature in C:" celsius)

#debugged code
# Enter temp in F:23
# #Temperatur in C: -5.0


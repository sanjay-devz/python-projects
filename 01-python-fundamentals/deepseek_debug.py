#the error code 

# fahrenheit = input("Enter temp in F:")
# celsius = (fahrenheit - 32) * 5/9
# print("Temperature in C:" celsius)

#debugged code
try:
    fahrenheit = float(input("Enter temp in F:"))
    celsius = (fahrenheit -32) * 5/9
    print("Temperatur in C:", round(celsius,2))

except ValueError:
    print("Invalid Input")



#output 
# #the error code 

# fahrenheit = input("Enter temp in F:")
# celsius = (fahrenheit - 32) * 5/9
# print("Temperature in C:" celsius)

#debugged code
# Enter temp in F:23
# #Temperatur in C: -5.0


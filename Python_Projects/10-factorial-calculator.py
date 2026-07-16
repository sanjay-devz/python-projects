# import math
 
# factor = math.factorial(5)

# print(factor)

def facorial_num(num):
    result = 1
    for i in range(2,num + 1 ):
        result *= i
    return result
a= facorial_num(4)
print(a)
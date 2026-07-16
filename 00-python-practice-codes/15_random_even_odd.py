import random
num = random.randint(1,100)
check = num % 2
if check == 0:
    print("The number is Even:",num)
else:
    print("The number is Odd:",num)

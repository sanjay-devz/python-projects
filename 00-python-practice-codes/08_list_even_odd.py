
#use append() to add "list1" with "list2"
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
thislist.append("hello")
print(thislist)

#add item from another list to same list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for Z in fruits:
  if Z.startswith("a"):
    print(fruits)

print(newlist)            
print("hello world")
for Y in fruits:
  if Y.endswith("a"):
    print(fruits)
  



#list comprehension one line for loopp 
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


#sting sort()

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#number sort()

listen = [100,23,54,81,67,24,99,789,245,564,465,352]
listen.sort(reverse = True)
print(listen)
print()


numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
numbers.append(60)
print(numbers)
numbers.remove(30)
print(numbers)


                           #maximum value in the list()
numbers = [23, 5, 78, 12, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

                            #minimum value in the list()
min_num = numbers[0]
for min in numbers:
    if min < min_num:
        min_num = min

print("Maximum:",max_num)
print("Minimum:",min_num)
"""



numbers = [10, 21, 34, 45, 60, 77, 80]

even_num = 0
odd_num = 0

#even numbers
for even in numbers:
    if even % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
        
        

       

print("Even number:",even_num)
print("Odd number:",odd_num)


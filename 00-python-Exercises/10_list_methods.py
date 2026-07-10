
#replace item in the list

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
print(len(thislist))
print(type(thislist))
print("#" * 25)

#replace two items with one value

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#using insert() methods

value = ["one","two","three","four","five","six"]
value.insert(0,"zero")
print(value)

#using append method() to add item at the last,
things = ['note','book','pen','pencil','box']
things.append('exampad')
things.insert(3,'earser')
print(things)



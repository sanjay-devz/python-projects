name = input("Enter Word:")
orignal = name


new_name = ""


for i in range(len(name)-1,-1,-1):
   new_name += name[i]

print(new_name)


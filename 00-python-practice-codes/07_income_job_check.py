name = input("Enter your name:").upper()
income = int(input("Enter your father anual income:"))
father_work = input("Enter your father job 'public' or 'private':")

if income <= 100000:
    if father_work == "public":
        print("you are eligible")
    else:
        print("not eligible")
elif income >= 100000:
    print("you are not eligible")
    if father_work == "private":
        print("you are not eligible")

print("#"*25)    
print("Name:",name)
print("Income:",income)
print("Father ocupation:",father_work)

print("#"*25)
name_user = input("Enter your name:").capitalize()
age = input("enter your age:")
if age < "18":
    print("not eligible")
else:
    print("you are eligible")
    mail_id = input("Enter your valid mail-id:").lower().replace(" ","")
    c = mail_id.endswith("@gmail.com")
    if c == True:
        print("valid mail-id")
        print(mail_id)
    elif c == False:
        outlook = input("Enter your outlook id:").lower()
        print(outlook)
        print("you are eligible")
    else:
        print("invalid mail id")
print('#'*24)
print("USER DETAILS")
print("Name:",name_user)
print("Age:",age)
print("Mail.id:",mail_id)
print('#'* 24)
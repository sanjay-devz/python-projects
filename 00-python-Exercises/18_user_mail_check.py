user_name = input("Enter your name:").capitalize()
user_age = input("Enter your age:")
age_check = user_age >= "18"
name_check = (len(user_name)) > 5
if age_check and name_check == True:
    email_id = input("Enter your valid mail-id:")
    if email_id.endswith("@gmail.com"):
        password = input("Enter a 8 chr password:")
        if password != 8:
            print("Invalid password")
        else:
            anth = input("Enter your profile:")
    else:
        print("your mail-id is banned contact helpline")
else:
    print("try again the name and age not attern our certaria")
    print("for quiry contact our helpline 233-232-443")

print("#" * 25)
print("user name:",user_name)
print("user age:",user_age)
print("user mail-id:",email_id)
print("password:",password)
print("#" * 25)


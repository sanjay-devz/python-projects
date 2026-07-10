email_id = input("Enter your email Address:").lower().strip()
name = input("Enter your name:").upper()
dob = int(input("Enter your age:"))
if dob < 18 :
  print("not valid")
else:
  print("G-mail:",email_id)
  print("Name:",name)
  print("Age:",dob)
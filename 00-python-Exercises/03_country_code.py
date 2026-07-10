couty = (input("Enter your country code:"))
phone_no = (input("Enter your phone no:"))

a = len(phone_no)           
if a == 10:   
  if couty == "+91" :           #to find country name,
    print("India")                      #By the country code.

  elif couty == "+48":
    print("Germany")

  elif couty == "+1":
    print("USA & Canada")

  elif couty == "+44":
    print("United Kingdom")
    

  elif couty == "+33":
    print("France")

else:
  print("Country not found")
  print(couty + phone_no)
print("phone number contain",a,"digits")

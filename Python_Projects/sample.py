num1 = 2
num2 = "df"

if isinstance(num1 or num2, str):
    print("failed")

else:
    print(num1 + num2)
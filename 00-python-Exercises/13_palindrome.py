
"""
num = 122
rever_num = 0

while num > 0:
    last_git = num % 10
    rever_num = (rever_num * 10) + last_git
    num = num // 10
    
print(rever_num)


a = 10
b = 20

c = a % b 
print(c)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        revers_num = 0

        while x > 0:
            last_digit = x % 10
            revers_num = (revers_num * 10) + last_digit
            x = x // 10

        return original == revers_num
    
    
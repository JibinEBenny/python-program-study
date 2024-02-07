num = int(input("Enter the number : "))         # user input
temp = num                                      # temp store the number given by the user
rev = 0                                         # variable to store the reverse of the string
while num != 0:                                 # loop ( While )
    rem = num % 10                              # to get the reminder of the number given by the user
    rev = 10 * rev + rem                        # to reverse the string
    num = num // 10                             # the '//' is used because the division should be floor
if temp == rev:                                 # compare both number
 print(temp, "--> Number is palindrome")
else:
 print(temp, "--> Not palindrome")

# <====OUTPUT====>
# Enter the number : 525
# 525 --> Number is palindrome
# Enter the number : 122
# 122 --> Not palindrome
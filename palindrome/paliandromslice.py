num = int(input("Enter the number : "))
#print(type(num))
temp = str(num)                                 # number to string
#print(type(temp))
rev = temp[::-1]                                # reversing using slicing [start:stop:increment]
#print(type(rev))
if temp == rev:                                 # compare both number
 print(temp, "--> Number is palindrome")
else:
 print(temp, "--> Not palindrome")


# <====OUTPUT====>
# Enter the number : 525
# 525 --> Number is palindrome
# Enter the number : 122
# 122 --> Not palindrome
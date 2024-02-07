1. paliandrome number by reversing the number

* rem = num % 10                              # to get the reminder of the number given by the user
* rev = 10 * rev + rem                        # to reverse the string
* num = num // 10                             # the '//' is used because the division should be floor

2. palindrome number using slicing 

* temp = str(num)                                 # number to string
* print(type(temp))
* rev = temp[::-1]                                # reversing using slicing [start:stop:increment]
* print(type(rev))
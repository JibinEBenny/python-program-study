
## Palindrome number

*A palindrome number is a number that remains the same when its digits are reversed. In other words, if you read a palindrome number from left to  right or from right to left, it will look the same.*  

***For example:***

*121 is a palindrome number because if you reverse it, it remains the same: 121.*  
*12321 is also a palindrome number.*  
*123 is not a palindrome number because if you reverse it, you get 321.*  
*Palindrome numbers are not limited to any specific number of digits and can be positive integers, but they can also include negative integers if we ignore the sign. For instance, -121 is also a palindrome number because when you remove the negative sign, the number remains the same.*  



**1. Paliandrome number by reversing the number**

```python 
* rem = num % 10                              # to get the reminder of the number given by the user
* rev = 10 * rev + rem                        # to reverse the string
* num = num // 10                             # the '//' is used because the division should be floor
```
**2. Palindrome number using slicing**

```python 
* temp = str(num)                                 # number to string
* print(type(temp))
* rev = temp[::-1]                                # reversing using slicing [start:stop:increment]
* print(type(rev))
```
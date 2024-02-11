## ODD or EVEN

*What are odd and even numbers with examples?*  

*Odd numbers are those numbers that cannot be divided into two equal parts,whereas even numbers are those numbers that can be divided into two equal parts.*  

***Examples:***  

*Odd numbers are 3, 5, 7, 9, 11, 13, 15,…*  
*Even numbers are 2, 4, 6, 8, 10, 12, 14,…*  

**1. Odd or Even ( divisable by 2 )**  

```python
if num % 2 == 0:              # Checks if the number is divisible by 2
    print(num,"---> Even number")
else:
    print(num,"---> Odd number")
```
**1. Odd or Even ( list )**  

```python
li = [1,2,3,4,5,6,7,8,9]
even = []                     # Empty list for Even number
odd = []                      # Empty list for odd number
for i in li :
    if(i > 0):
        if i % 2 == 0 :       # Checks if the number is divisible by 2
            even.append(i)
        else:
            odd.append(i)
```
## Fibonacci numbers

*The Fibonacci numbers are a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes as follows:*  
*0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...*  

*So, for instance, the third Fibonacci number is 1 (0 + 1), the fifth is 3 (1 + 2), and so on. This sequence can be defined recursively by the formula:*  

*F(n) = F(n-1) + F(n-2)*  

*where F(n) represents the nth Fibonacci number, and F(0) = 0 and F(1) = 1 are the base cases.*  

**1.  Fibonacci series using list**

```python
 for i in range(0,num-1,1):            # to loop within the range
     sum = fib[i] + fib[i+1]           # to add the adjacent numbers
     fib.append(sum)                   # for appending to the list
```
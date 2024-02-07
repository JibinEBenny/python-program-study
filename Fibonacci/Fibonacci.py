num = int(input("Enter the length of Fibonacci sereis : "))
fib = [0,1]                      # list with the 0,1 as default

for i in range(0,num-1,1):       # to loop within the range
    sum = fib[i] + fib[i+1]      # to add the adjacent numbers
    fib.append(sum)              # for appending to the list

print("The top "+str(num)+" numbers of Fibonacci series is : ",fib)

# <====OUTPUT====>
# Enter the length of Fibonacci sereis : 20
# The top 20 numbers of Fibonacci series is :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
num = int(input("Enter the length of Fibonacci sereis : "))
fib = [0,1]                      # list with the 0,1 as default

for i in range(0,num-1,1):       # to loop within the range
    sum = fib[i] + fib[i+1]      # to add the adjacent numbers
    fib.append(sum)              # for appending to the list

print("The top "+str(num)+" numbers of Fibonacci series is : ",fib)
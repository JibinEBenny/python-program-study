num = 5#int(input("Enter the number to check if the number is odd or even : "))
if(num > 0):
    if num % 2 == 0 :                                                                       # Checks if the number is divisible by 2
        print(num,"---> Even number")
    else:
        print(num,"---> Odd number")
else:
    print("Enter number greater than 0")

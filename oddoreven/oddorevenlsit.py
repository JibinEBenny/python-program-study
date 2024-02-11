li = [-1,-2,0,1,2,3,4,5,6,7,8,9]
Nu, even, odd = [], [], []
for i in li :
    if(i > 0):                          # check if the number is greater than 0
        if i % 2 == 0 :                 # Checks if the number is divisible by 2
            even.append(i)              # appending number to list of even numbers
        else:
            odd.append(i)               # appending number to list of even numbers
    else:
        Nu.append(i) 
print("Even :",even)
print("Odd :",odd)
print("Number less than one :",Nu)


# <------------- ANOTHER METHOD ---------->


# li = [-1,-2,0,1,2,3,4,5,6,7,8,9]
# Nu, even, odd = [], [], []
# even = [i for i in li if i > 0 and i % 2 == 0]
# odd = [i for i in li if i > 0 and i % 2 != 0]
# Nu = [i for i in li if i <= 0]
# print("Even :",even)
# print("Odd :",odd)
# print("Number less than one :",Nu)
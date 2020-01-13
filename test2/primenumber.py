## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor


for num in check_prime:
    factor=0
    i=1
    while i <= num:
        if num % i ==0:
            factor+=1
            if factor > 2:
                print("{}  is NOT a prime number, because {} is a factor of {}".format(num,i,num))
                break
        i+=1
    if factor==2:
        print("{} is a Prime Number".format(num))

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:
            print("{} IS a prime number".format(num))
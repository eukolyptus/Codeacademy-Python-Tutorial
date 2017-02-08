"""
Function isPrime(x) takes a number parameter x 
and determines if it is prime or not 
"""

def isPrime(x):
    if (x < 2):
        return False
    elif (x == 2):
        return True
    else:
        for i in range(2, x, 1):
            if i == x-1:
                return True

            if (x % i) == 0:
                return False
               
    return True


#Test Cases here
print "Is 4 prime? ", isPrime(4) 

for x in range(15):
	print ("#: "), x, ("\tis prime: "), isPrime(x)
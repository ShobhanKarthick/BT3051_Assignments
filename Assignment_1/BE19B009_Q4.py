
n = input("Enter the number for which you need factors for: ")
def prime_factors(n):
    prime_factors = []
    for i in range(2, n+1):
        if(n%i == 0 ):                              # Checking if divisible
            prime_list = []
            for j in range(2, i):
                prime_list.append(i%j)
            if(all(prime_list)):                    # Checking if the factor is prime number
                prime_factors.append(i)             
        else:
            continue    
    return prime_factors

try:
    n = int(n)
except:
    print("Please enter a valid number!")

if(n < 0):
    print("Sorry! I only accept negative numbers")
    exit()

if(n > 1000000):
    print("Enter a number below 1000000")
    exit()

if(n == 1 or n == 0):
    print("Do you really want prime factors for {0} ?!".format(n))
else:
    factors = prime_factors(n)
    print(factors)
            
        

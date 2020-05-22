  
prime_sieve = []
for x in range (0,1005):
    prime_sieve.append(0)

for i in range (2,1001):
    if(prime_sieve[i]==0): #if values is 0 no. is a prime
        print(i)
        for j in range (2*i,1001,i): # mark all its mutiples as they wont be primes
            prime_sieve[j]=1

def count_primes(n):  #count number of prime a number is divisible by
    c=0;
    for i in range (2,n+1):
        if(n%i==0):
            c=c+1
            while(n%i==0):
                n=n/i


    return c

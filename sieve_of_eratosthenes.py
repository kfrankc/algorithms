# Sieve of Eratosthenes

# This ancient algorithm can find all prime numbers up to any given limit.
# It does so by iteratively marking as composite the multiples of each prime, starting with the prime number 2.
    
def sieve_of_eratosthenes(A):
    primary_list = [True] * A
    primary_list[0] = primary_list[1] = False

    for (i, isPrime) in enumerate(primary_list):
        if isPrime:
            print i
            for n in xrange(i*i, A, i):
                primary_list[n] = False

sieve_of_eratosthenes(20)

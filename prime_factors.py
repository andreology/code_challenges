#write a python function to find all prime factors of N

def get_primes(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors

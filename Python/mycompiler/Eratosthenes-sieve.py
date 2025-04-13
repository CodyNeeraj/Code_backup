# Seive of Eratosthenes
from math import sqrt
def primes_less_than(n):
    if n<= 2:
        return []
    is_prime = list(range(0,n))
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n)+1)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]

if __name__ == '__main__':
    # lis = primes_less_than(1000000)
    # fact only 7.84 of number in the above range of million integers are prime !!
    # print(len(lis))
            lisy = primes_less_than(2000000)
    print(sum(lisy))

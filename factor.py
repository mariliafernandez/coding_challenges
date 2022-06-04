def factor(num):

    prime = 2
    factors = []

    while num != 1:
        if num % prime == 0:
            factors.append(prime)
            num = num / prime
        else:
            prime += 1

    return factors


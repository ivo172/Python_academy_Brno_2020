def list_primes(to):
    primes = ''
    for num in range(2, to + 1):
       if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes = primes + ' ' + str(num)
    primes = (primes.strip())
    primes = (primes.split())
    print(primes)
    return primes


def is_prime(number):
    return str(number) in list_primes(number)


print(list_primes(500))
# print(is_prime(41))

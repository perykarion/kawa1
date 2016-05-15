'''
I am well aware that valid answer does not exist, since all natural numbers divide by 1 and 1 is not prime.
Secondly, even if we exclude 1 from our reasoning, still only primes are valid answers.
All numbers have themselves as divisors therefore all non-primes have at least non-prime divisor.
So I have excluded that as well (as was settled).

'''


__author__ = 'maslowska'
__version__ = '0.1'

import numbers_with_prime_divisors

def main(number):
    return numbers_with_prime_divisors.get_numbers_with_prime_divisors(number)
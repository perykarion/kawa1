import math


def get_divisors(number):
    divisors_list = [number]
    for potential_divisor in range(2, number/2+1):
        if number % potential_divisor == 0:
            divisors_list.append(potential_divisor)
    return divisors_list



def is_prime(number):
    if number == 2 or (number > 2 and number % 2 != 0):
        for value in range (3, int(math.sqrt(number)) + 1):
            if number % value == 0:
                return False
        return True
    else:
        return False


def is_natural(number):
    if number > 0 and type(number) in (int, long):
        return True
    else:
        return False


def has_prime_divisors_only(number):
    divisors = get_divisors(number)
    for divisor in divisors:
        if (divisor != number) and (not is_prime(divisor)):
            return False
    return True


def get_numbers_with_prime_divisors(number):
    numbers_with_prime_divisors = []
    if is_natural(number):
        for value in range(2, number+1):
            if has_prime_divisors_only(value):
               numbers_with_prime_divisors.append(value)
    else:
        print "Nice try :P"
    return numbers_with_prime_divisors








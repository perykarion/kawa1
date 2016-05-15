import unittest
import numbers_with_prime_divisors

class IsNaturalTestCase(unittest.TestCase):
    def test_is_natural_negative(self):
        test_values = [-5, -2.5, 0, 2.5, "a", (4, 6)]
        for number in test_values:
            self.assertFalse(numbers_with_prime_divisors.is_natural(number)), "Number at test is: {}".format(number)

    def test_is_natural_positive(self):
        test_numbers = [1, 45, 1000]
        for number in test_numbers:
            for number in test_numbers:
                self.assertTrue(numbers_with_prime_divisors.is_natural(number)), "Number at test is: {}".format(number)


class GetDivisorsTestCase(unittest.TestCase):
    def test_get_divisors(self):
        test_values = {2 : [2], 3 : [3], 4 : [4, 2], 5 : [5], 6 : [6, 2, 3], 7: [7], 8 : [8, 2, 4]}
        for value in test_values:
            answer = numbers_with_prime_divisors.get_divisors(value)
            self.assertEqual(test_values[value], answer)

class IsPrime(unittest.TestCase):
    def test_num_less_than_three(self):
        numbers_too_small = [0, 1, 2]
        for number in numbers_too_small:
            self.assertFalse(numbers_with_prime_divisors.is_prime(number))

    def test_even_numbers(self):
        even_numbers = [2, 4, 8]
        for number in even_numbers:
            self.assertTrue(number % 2 == 0)

    def test_odd_numbers(self):
        odd_numbers = [5, 7, 9]
        for number in odd_numbers:
            self.assertFalse(number % 2 == 0)

    def test_primes(self):
        primes = [3, 5, 7, 11, 13, 15]
        for value in primes:
            self.assertTrue(numbers_with_prime_divisors.is_prime(value))

    def test_not_primes(self):
        not_primes = [4, 10, 22, 169, 0]
        for value in not_primes:
            self.assertFalse(numbers_with_prime_divisors.is_prime(value))

class NumbersWithPrimeDivisors(unittest.TestCase):
    def test_nums_with_prime_divisors(self):
        test_values = {0 : [], 1 : [], 2 : [2], 3 : [2, 3], 4 : [2, 3, 4], 5 : [2, 3, 4, 5], 6 : [2, 3, 4, 5, 6]}

        for value in test_values:
            answer = numbers_with_prime_divisors.get_numbers_with_prime_divisors(value)
            self.assertEqual(test_values[value], answer)


if __name__ == '__main__':
    unittest.main()
import itertools
from collections import Counter
from typing import Generator
from functools import reduce
import operator


def test(func, dataset):
    for data in dataset:
        try:
            iter(data)
            print(func(*data))
        except Exception:
            print(func(data))


def factors_all(num):
    result = []
    for i in range(1, int(num ** 0.5) + 1):
        if (num / i).is_integer():
            result.extend([i, num // i])
    return sorted(result)


# test(factors_all, [113, 117, 119, 36, 200, 588, 576])


def find_all_factors(number):
    result, divisor = [], 1
    while number / divisor >= divisor:
        quotient = number / divisor
        if quotient.is_integer():
            result.extend([divisor, int(quotient)])
        divisor += 1
    return sorted(result)


# test(find_all_factors, [12, 36, 98, 117, 378, 219])


def generate_prime(upper) -> Generator:
    for i in range(2, upper + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if (i / j).is_integer():
                break
        else:
            yield i

# print(list(generate_prime(17)))
# print(list(generate_prime(16)))
# print(list(generate_prime(18)))
# print(list(generate_prime(15)))
# print(list(generate_prime(50)))
# print(list(generate_prime(2)))
# print(list(generate_prime(3)))


def is_prime(num):
    """prime number and composite number"""
    for i in range(2, int(num ** 0.5) + 1):
        if (num / i).is_integer():
            return False
    else:
        return True


# test(is_prime, [113, 117, 119, 111, 2, 3, 5])


def is_prime_v2(num):
    """
    1)  Test each of the primes, in order, to see if it is a factor of the number.
    2)  Start with 2 and stop when the quotient is smaller than the divisor 
        or when a prime factor is found.
    3)  If the number has a prime factor, then it is a composite number. 
        If it has no prime factors, then the number is prime.
    """
    if num == 2:
        return True
    for prime in generate_prime(int(num ** 0.5) + 1):
        if (num / prime).is_integer():
            return False
    else:
        return True


# test(is_prime_v2, [997, 137, 2, 3, 219, 51])


def prime_factorization_tree(num):
    """
    1)  Find any factor pair of the given number, and use these numbers to
        create two branches.
    2)  If a factor is prime, that branch is complete. Circle the prime.
    3)  If a factor is not prime, write it as the product of a factor pair
        and continue the process.
    4)  write the composite number as the product of all the cicled primes.
    """
    
    def _helper(num):
        if is_prime(num):
            return [num]
        else:
            factors = factors_all(num)
            mid_len = len(factors) // 2
            return _helper(factors[mid_len]) + _helper(factors[mid_len - 1])
    
    return sorted(_helper(num))


# test(
#     prime_factorization_tree, 
#     [36, 48, 999, 1001, 126, 294, 2160, 1080]
# )


def prime_after_num(num):
    for i in itertools.count(num + 1, 1):
        if is_prime(i):
            return i


def prime_factorization_ladder_method(num):

    def _helper(num, prime):
        if is_prime(num):
            return [num]
        else:
            while not (num / prime).is_integer():
                prime = prime_after_num(prime)
            return _helper(num // prime, prime) + [prime]
        
    return sorted(_helper(num, 2))


# test(
#     prime_factorization_ladder_method, 
#     [120, 48, 154, 759, 126, 294, 2475]
# )


def lcm(num_a, num_b):
    """Least Common Multiple"""
    if num_a == num_b:
        return num_a
    smaller, greater = min(num_a, num_b), max(num_a, num_b)
    for i in range(1, smaller + 1):
        if (greater * i / smaller).is_integer():
            return greater * i


# test(lcm, [(15, 20), (9, 12), (18, 24)])


def lcm_prime_factor_method(num_a, num_b):
    prime_factors_a, prime_factors_b = (
        prime_factorization_tree(num_a),
        prime_factorization_ladder_method(num_b)
    )
    res = []
    counter_a, counter_b = Counter(prime_factors_a), Counter(prime_factors_b)
    for key in counter_a | counter_b:
        if key in counter_b and key in counter_a:
            res += [key] * max(counter_a[key], counter_b[key])
        else:
            if key in counter_a:
                key_quantity = counter_a[key]
            if key in counter_b:
                key_quantity = counter_b[key]
            res += [key] * key_quantity
    return reduce(operator.mul, res)


# test(
#     lcm_prime_factor_method, 
#     [
#         (12, 18), (15, 18), (12, 20), (84, 90),
#         (15, 35), (50, 100), (55, 88), (60, 72), (8, 10)
#     ]
# )


def medians(dataset):
    import statistics
    averages = ("mean", "median", "mode")
    for op in averages:
        print(f"{op.capitalize()}: {getattr(statistics, op)(dataset)}")


# medians(
#     [2, 3, 3, 5, 8, 8, 8, 12, 15, 15]
# )


def greatet_common_factor(num_a, num_b):
    if num_a == num_b:
        return num_a
    if is_prime(num_a) or is_prime(num_b):
        return 1
    prime_factors_a, prime_factors_b = (
        prime_factorization_tree(num_a),
        prime_factorization_tree(num_b)
    )
    result = []
    counter_a, counter_b = Counter(prime_factors_a), Counter(prime_factors_b)
    for key in counter_a & counter_b:
        result += [key] * min(counter_a.get(key, 0), counter_b.get(key, 0))
    return reduce(operator.mul, result)


# print(greatet_common_factor(24, 36))
# print(greatet_common_factor(36, 54))
# print(greatet_common_factor(48, 80))
# print(greatet_common_factor(41, 80))


def integer_reverse(integer):
    res = 0
    while integer != 0:
        res = res * 10 + integer % 10
        integer //= 10
    return res


# print(integer_reverse(15273))


if __name__ == "__main__":
    pass
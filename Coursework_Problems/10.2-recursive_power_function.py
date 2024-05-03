def recursive_power(number, to_the_power_of):
    if to_the_power_of == 1:
        return number

    return number * recursive_power(number, to_the_power_of - 1)


def recursive_power_with_square(x, n):
    if n == 1:
        return x
    if n & 1 == 0:
        return recursive_power_with_square(x, int(n / 2)) ** 2
    if n & 1 == 1:
        return x * recursive_power_with_square(x, int(n // 2)) ** 2


print(recursive_power(2, 10))
print(recursive_power_with_square(2, 10))

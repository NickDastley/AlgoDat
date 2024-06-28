def my_hash(number):
    this_hash = (3 * number + 5) % 11
    print(number, this_hash)
    return this_hash


numbers = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]


for number in numbers:
    my_hash(number)

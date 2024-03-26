# P-1.30 Write a Python program
# that can take a positive integer
# greater than 2 as input
# and write out the number of times
# one must repeatedly divide this number by 2
# before getting a value less than 2.
def dividing_by_two(positive_integer):
    number_of_divisions = 0

    while True:
        positive_integer /= 2
        # OR number = number / 2

        number_of_divisions += 1

        if positive_integer < 2:
            return number_of_divisions

print(dividing_by_two(2048))
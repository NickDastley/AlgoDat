# R-1.4 Write a short Python function
# that takes a positive integer n
# and returns the sum of the squares
# of all the positive integers smaller than n.

def square_sum(positive_integer):
    squaredSum = 0
    for i in range (1, positive_integer):
        squaredSum = squaredSum + i * i
        # ODER squaredSum += (i ** 2)
    return squaredSum

print(square_sum(12))
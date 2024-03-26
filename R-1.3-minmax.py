# R-1.3 Write a short Python function,
# minmax(data), that takes a sequence of one
# or more numbers, and returns the smallest and
# largest numbers, in the form of a tuple of
# length two. Do not use the built-in
# functions min or max in implementing your
# solution.

def minmax(numberList):
    current_min = current_high = numberList[0]
    for number in numberList:
        if current_min > number:
            current_min = number
        if current_high < number:
            current_high = number

    return current_min, current_high


print(minmax([1, 2, 3, 8, 4, 7, 2]))

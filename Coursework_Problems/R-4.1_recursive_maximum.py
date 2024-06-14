# R-4.1 Describe a recursive algorithm
# for finding the maximum element in a sequence S,
# of n elements. What is your running time and space usage?

# running Time = O(n)
# space usage = O(n)

def recursive_maximum(sequence, n):
    if n == len(sequence) - 1:
        return sequence[n]

    a = sequence[n]
    b = recursive_maximum(sequence, n + 1)
    if a > b:
        return a
    else:
        return b


print(recursive_maximum([1, 2, 30, 4, 5, 70, 10], 0))
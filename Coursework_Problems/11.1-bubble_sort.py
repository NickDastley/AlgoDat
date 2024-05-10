# The bubble sort implementation we discussed in class
# has a best-case running time complexity of O(n^2)
# Implement a better bubble sort that has a best-case running time complexity of O(n)
def bubble_sort(A):
    n = len(A)
    for i in range(n):
        rearranged = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                rearranged = True
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp
        if not rearranged:
            return

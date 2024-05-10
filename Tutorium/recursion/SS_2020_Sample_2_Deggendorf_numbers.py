def deg(n):
    if 0 < n <= 3:
        return 1

    return deg(n - 1) + deg(n - 2) + deg(n - 3)


for i in range(4, 10):
    print(str(i) + ": " + str(deg(i)))
    pass

# b) Derive the worst-case running time complexity:
# O(3^n)

# c) reimplement your algorithm in Python using a top-down dynamic programming approach.
memory = {0: 1, 1: 1, 2: 1};


def deg2(n):
    if n not in memory:
        memory[n] = deg2(n - 1) + deg2(n - 2) + deg2(n - 3)
    return memory[n]


for i in range(4, 10):
    print(str(i) + ": " + str(deg2(i)))
    pass

# d) bottom-up approach
def deg3(n):
    if n < 4:
        return 1
    for i in range(4, n + 1):
        memory[i] = memory[i - 1] + memory[i - 2] + memory[i - 3]
    return memory[n]

def dit(n):
    if 0 <= n <= 4:
        return 1

    return (dit(n - 1) + dit(n - 2)
            + dit(n - 3) + dit(n - 4)
            + dit(n - 5))


for i in range(10):
    print(dit(i))

# c) top-down dyanmic programming approach
memory = {0: 1,
          1: 1,
          2: 1,
          3: 1,
          4: 1}


def dit2(n):
    if n in memory:
        return memory[n]

    memory[n] = dit2(n - 1) + dit2(n - 2) + dit2(n - 3) + dit2(n - 4) + dit2(n - 5)
    return memory[n]

# d) bottom-up
def dit3(n):
    if 0 <= n <= 4:
        return 1
    prev_dit1 = 1
    prev_dit2 = 1
    prev_dit3 = 1
    prev_dit4 = 1
    current_dit = 1
    for i in range(n-4):
        new_dit = prev_dit1 + prev_dit2 + prev_dit3 + prev_dit4 + current_dit
        prev_dit1 = prev_dit2
        prev_dit2 = prev_dit3
        prev_dit3 = prev_dit4
        prev_dit4 = current_dit
        current_dit = new_dit
    return current_dit

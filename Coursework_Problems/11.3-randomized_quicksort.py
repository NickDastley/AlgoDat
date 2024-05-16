import random
import time


def quick_sort(data):
    if len(data) <= 1:
        return data

    random_pivot_position = random.randint(0, len(data) - 1)
    pivot = data[random_pivot_position]

    left_sequence = []
    right_sequence = []

    for element in data:
        if element < pivot:
            left_sequence.append(element)
        elif element >= pivot:
            right_sequence.append(element)

    return quick_sort(left_sequence) + [pivot] + quick_sort(right_sequence[1:])


list = []

for _ in range(10000):
    list.append(random.randint(0, 1000))

print(list)
print(len(list))
start_time = time.time()
sorted_list = quick_sort(list)
print((time.time() - start_time) * 1000)
print(sorted_list)
print(len(sorted_list))
start_time = time.time()
quick_sort(sorted_list)
print((time.time() - start_time) * 1000)

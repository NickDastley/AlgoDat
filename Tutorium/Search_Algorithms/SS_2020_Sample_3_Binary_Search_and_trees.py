def search_binary(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return True

        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


print(search_binary([0, 1, 2, 4, 4, 5, 5, 5, 6, 7, 8, 9], 2))

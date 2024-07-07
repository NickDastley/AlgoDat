def search_binary_iterative(data, target):
    low = 0
    high = len(data) - 1

    while True:
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
import sys # provides getsizeof function

data = []

for k in range (26):
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None) # increase length by one
import sys # provides getsizeof function

data = []
last_bytesize = 0

for k in range (26):
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes

    if b > last_bytesize:
        last_bytesize = b
        print("List has expanded at " + str(a))

    data.append(None) # increase length by one
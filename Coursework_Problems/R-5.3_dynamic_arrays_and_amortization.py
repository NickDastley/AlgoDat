import sys # provides getsizeof function

data = []

for i in range(26):
    data.append(None)

last_bytesize = sys.getsizeof(data)

for k in range(len(data)):
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes

    if b < last_bytesize:
        last_bytesize = b
        print("List has shrunk at " + str(a))

    data.pop(0)
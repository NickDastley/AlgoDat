def remove_all(data, value):
    new_data = []
    for entry in data:
        if entry != value:
            new_data.append(entry)
    return new_data
    pass

data = []

for i in range(10):
    data.append(i)

print(data)
data.remove(4)
print(data)
data.append(5)
data.append(5)
data.append(5)
data.append(6)
data.append(6)
data.append(6)
data.append(5)
data.append(5)
data.append(5)
print(data)
data = remove_all(data, 5)
print(data)
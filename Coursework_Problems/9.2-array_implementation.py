import ctypes


## TODO implement __setitem__(self, k, value), insert(self, k, value) "prüfen ob Platz ist, und alles nach rechts verschieben", remove(self, k)

class MyArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def __setitem__(self, key, value):  # Element überschreiben
        if self._n - 1 < key:
            raise IndexError('invalid index')
        self._A[key] = value
        return

    def insert(self, key, value):
        if not 0 <= key < self._n:
            raise IndexError('invalid index')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        # Alle danach kommenden Einträge nach hinten verschieben
        self.append("dummy")
        i = self._n - 1
        while (i != key):
            self.__setitem__(i, self._A[i - 1])
            i -= 1

        self.__setitem__(key, value)
        return

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
        return

    def remove(self, key):
        # i = key
        # while (i < self._n):
        #     if i + 1 < self._n:
        #         self.__setitem__(i, self._A[i + 1])
        #         i += 1
        #     else:
        #         self._A[i] = None
        #         break
        # self._n -= 1
        # return
        newArray = self._make_array(self._capacity)
        for i in range(len(self._A) - 2):
            if i < key:
                newArray[i] = self._A[i]
            else:
                newArray[i] = self._A[i + 1]
        self._A = newArray
        return

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    arr = MyArray()
    arr.append(5)
    arr.append(6)
    arr.append(7)
    arr.insert(2, 10)
    arr.append("Döner")
    arr.remove(2)
    print(arr)

class LinkedList:
    class _Node:
        def __init__(self, element):
            self._element = element
            self._next_element = None

    def __init__(self):
        self._head = None
        self._size = 0

    # a)
    def add(self, element):
        new_node = self._Node(element)
        if self._head is None:
            self._head = new_node
        else:
            current_node = self._head

            while current_node._next_element is not None:
                current_node = current_node._next_element
            current_node._next_element = element

        self._size += 1

    # b)
    def remove_first(self):
        if self._size == 0:
            raise IndexError('Linked list is empty')

        self._head = self._head._next_element
        self._size -= 1

    # c)
    def __iter__(self):
        current_node = self._head
        while current_node is not None:
            yield current_node
            current_node = current_node._next_element

    # d)
    # Benefits of LinkedLists:
    # - Fast insertions and deletions of elements
    # - No need of resizing
    #
    # Benefits of ArrayLists:
    # - Fast access on elements with index (O(1))
    # - Requires less memory than linked lists

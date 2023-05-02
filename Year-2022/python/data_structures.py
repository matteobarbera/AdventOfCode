class Node:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

    def __str__(self):
        has_next = self.next is not None
        return f"data={self.data} has_next={has_next}"


class DoubleNode:
    def __init__(self, data, *, previous_n=None, next_n=None):
        self.data = data
        self.previous = previous_n
        self.next = next_n

    def __str__(self):
        has_prev = self.previous is not None
        has_next = self.next is not None
        return f"data={self.data} has_prev={has_prev} has_next={has_next}"


class LinkedList:

    def __init__(self, arr: list = None):
        self.head = None
        self.tail = None
        self.size = 0

        if arr is not None:
            self._from_array(arr)

    def _from_array(self, arr: list):
        prev_node = None
        for el in arr:
            if prev_node is not None:
                node = Node(el)
                prev_node.next = node
            else:
                node = Node(el)
                self.head = node
            prev_node = node
        self.tail = node
        self.size = len(arr)

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def append_left(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def at_index(self, item):
        if item >= self.size:
            raise IndexError("node index out of range")
        if item < 0:
            raise NotImplementedError("negative indices unsupported")
        node = self.head
        while item > 0:
            node = node.next
            item -= 1
        return node

    def __getitem__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return node
            node = node.next
        raise KeyError(item)

    def __setitem__(self, key, value):
        node = self.head
        while node is not None:
            if node.data == key:
                node.data = value
        raise KeyError(key)

    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        nodes = []
        node = self.head
        while node.next is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(node.data)
        return str(nodes)


class CircularLList:
    def __init__(self, arr):
        self.head = None
        self.size = 0
        self._from_array(arr)

    def _from_array(self, arr: list):
        prev_node = None
        for el in arr:
            node = Node(el)
            if prev_node is not None:
                prev_node.next = node
            else:
                self.head = node
            prev_node = node
        node.next = self.head
        self.size = len(arr)

    def at_index(self, item):
        if item >= self.size:
            raise IndexError("node index out of range")
        if item < 0:
            raise NotImplementedError("negative indices unsupported")
        node = self.head
        while item > 0:
            node = node.next
            item -= 1
        return node

    def __getitem__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return node
            node = node.next
        raise KeyError(item)

    def __setitem__(self, key, value):
        node = self.head
        while node is not None:
            if node.data == key:
                node.data = value
        raise KeyError(key)

    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        node = self.head
        nodes = []
        while node.next is not self.head:
            nodes.append(node.data)
            node = node.next
        nodes.append(node.data)
        return str(nodes)


class DoubleLList:

    def __init__(self, arr: list = None):
        self.head = None
        self.tail = None
        self.size = 0

        if arr is not None:
            self._from_array(arr)

    def _from_array(self, arr: list):
        node_1 = None
        for el in arr:
            if node_1 is not None:
                node = DoubleNode(el, previous_n=node_1)
                node_1.next = node
            else:
                node = DoubleNode(el)
                self.head = node
            node_1 = node
        self.tail = node
        self.size = len(arr)

    def append(self, data):
        node = DoubleNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def append_left(self, data):
        node = DoubleNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.size += 1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __reversed__(self):
        node = self.tail
        while node is not None:
            yield node.data
            node = node.previous

    def at_index(self, item):
        if item >= self.size:
            raise IndexError("node index out of range")
        if item < 0:
            raise NotImplementedError("negative indices unsupported")
        node = self.head
        while item > 0:
            node = node.next
            item -= 1
        return node

    def __getitem__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return node
            node = node.next
        raise KeyError(item)

    def __setitem__(self, key, value):
        node = self.head
        while node is not None:
            if node.data == key:
                node.data = value
        raise KeyError(key)

    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        nodes = []
        node = self.head
        while node.next is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(node.data)
        return str(nodes)


class CircularDLList:

    def __init__(self, arr: list):
        self.head = None
        self.size = 0

        if arr is not None:
            self._from_array(arr)

    def _from_array(self, arr: list):
        node_1 = None
        for el in arr:
            if node_1 is not None:
                node = DoubleNode(el, previous_n=node_1)
                node_1.next = node
            else:
                node = DoubleNode(el)
                self.head = node
            node_1 = node
        node.next = self.head
        self.head.previous = node
        self.size = len(arr)

    def at_index(self, item):
        if item >= self.size:
            raise IndexError("node index out of range")
        if item < 0:
            raise NotImplementedError("negative indices unsupported")
        node = self.head
        while item > 0:
            node = node.next
            item -= 1
        return node

    def __getitem__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return node
            node = node.next
        raise KeyError(item)

    def __setitem__(self, key, value):
        node = self.head
        while node is not None:
            if node.data == key:
                node.data = value
        raise KeyError(key)

    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        nodes = []
        node = self.head
        while node.next is not self.head:
            nodes.append(node.data)
            node = node.next
        nodes.append(node.data)
        return str(nodes)


if __name__ == "__main__":
    pass

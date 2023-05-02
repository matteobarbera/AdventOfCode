import unittest

from data_structures import *


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.test_arr = [0, 1, 2, 3]
        self.llst = LinkedList(self.test_arr)

    def test_from_array(self):
        self.assertEqual(str(self.llst), str(self.test_arr))
        self.assertEqual(self.llst.size, len(self.test_arr))

    def test_iter(self):
        for i, j in zip(self.llst, self.test_arr):
            self.assertEqual(i, j)

    def test_getitem(self):
        self.assertEqual(self.llst[2], 2)

    def test_at_index(self):
        self.assertEqual(self.llst.at_index(1).data, 1)

    def test_setitem(self):
        self.llst[1] = 5
        self.assertEqual(self.llst.at_index(1).data, 5)

    def test_append(self):
        self.llst.append(4)
        self.assertEqual(self.llst[4], self.llst.tail)
        self.assertEqual(self.llst.tail.data, 4)
        self.assertEqual(self.llst[3].next, self.llst.tail)

    def test_append_left(self):
        self.llst.append_left(4)
        self.assertEqual(self.llst[4], self.llst.head)
        self.assertEqual(self.llst.head.data, 4)
        self.assertEqual(self.llst[4].next, self.llst[0])


class TestCircularLList(unittest.TestCase):

    def setUp(self) -> None:
        self.test_arr = [0, 1, 2, 3]
        self.llst = CircularLList(self.test_arr)

    def test_from_array(self):
        self.assertEqual(str(self.llst), str(self.test_arr))
        self.assertEqual(self.llst.size, len(self.test_arr))

    def test_getitem(self):
        self.assertEqual(self.llst[2], 2)

    def test_at_index(self):
        self.assertEqual(self.llst.at_index(1).data, 1)

    def test_circularity(self):
        self.assertEqual(self.llst[3].next, self.llst.head)

    def test_setitem(self):
        self.llst[1] = 5
        self.assertEqual(self.llst.at_index(1).data, 5)


class TestDoubleLList(unittest.TestCase):

    def setUp(self) -> None:
        self.test_arr = [0, 1, 2, 3]
        self.llst = DoubleLList(self.test_arr)

    def test_from_array(self):
        self.assertEqual(str(self.llst), str(self.test_arr))
        self.assertEqual(self.llst.size, len(self.test_arr))

    def test_iter(self):
        for i, j in zip(self.llst, self.test_arr):
            self.assertEqual(i, j)

    def test_reversed(self):
        for i, j in zip(reversed(self.llst), reversed(self.test_arr)):
            self.assertEqual(i, j)

    def test_getitem(self):
        self.assertEqual(self.llst[2], 2)

    def test_at_index(self):
        self.assertEqual(self.llst.at_index(1).data, 1)

    def test_setitem(self):
        self.llist[1] = 5
        self.assertEqual(self.llist.at_index(1).data, 5)

    def test_append(self):
        self.llst.append(4)
        self.assertEqual(self.llst[4], self.llst.tail)
        self.assertEqual(self.llst.tail.data, 4)
        self.assertEqual(self.llst[3].next, self.llst.tail)
        self.assertEqual(self.llst.head.previous, self.llst.tail)

    def test_append_left(self):
        self.llst.append_left(4)
        self.assertEqual(self.llst[4], self.llst.head)
        self.assertEqual(self.llst.head.data, 4)
        self.assertEqual(self.llst[4].next, self.llst[0])
        self.assertEqual(self.llst.tail.next, self.llst.head)


class TestCircularDLList(unittest.TestCase):

    def setUp(self) -> None:
        self.test_arr = [0, 1, 2, 3]
        self.llst = CircularDLList(self.test_arr)

    def test_from_array(self):
        self.assertEqual(str(self.llst), str(self.test_arr))
        self.assertEqual(self.llst.size, len(self.test_arr))

    def test_getitem(self):
        self.assertEqual(self.llst[2], 2)

    def test_at_index(self):
        self.assertEqual(self.llst.at_index(1).data, 1)

    def test_circularity(self):
        self.assertEqual(self.llst[3].next, self.llst.head)
        self.assertEqual(self.llst.head.previous, self.llst[3])

    def test_setitem(self):
        self.llist[1] = 5
        self.assertEqual(self.llist.at_index(1).data, 5)


if __name__ == "__main__":
    unittest.main()

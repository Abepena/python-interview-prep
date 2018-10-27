import unittest


class Deque:
    """Python implementation of a deque using built-in list
    (without using collections.deque)"""

    def __init__(self, *items):
        self.items = list(items)

    def append_left(self, element):
        """Add element to the front (left) of the Deque"""
        self.items.insert(0, element)

    def pop_left(self):
        """Remove element from the front (left) of the Deque"""
        return self.items.pop(0)

    def append(self, element):
        """Add element to the end (right) of the Deque"""
        self.items.append(element)

    def pop(self):
        """Remove element from the end (right) of the Deque"""
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        items = ", ".join([str(item) for item in self.items])
        return f'Deque({items})'


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.deque = Deque(1, 2, 3)
        self.empty_deque = Deque()

    def test_append_left(self):
        self.deque.append_left(0)
        self.assertEqual(str(self.deque), 'Deque(0, 1, 2, 3)')

    def test_pop_left(self):
        self.assertEqual(self.deque.pop_left(), 1)

    def test_append(self):
        self.deque.append(4)
        self.assertEqual(str(self.deque), 'Deque(1, 2, 3, 4)')

    def test_size(self):
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.empty_deque.size(), 0)


if __name__ == '__main__':
    unittest.main()

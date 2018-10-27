import unittest


class Stack:
    """Python implementation of a stack using built-in lists"""

    def __init__(self, *items):
        self.items = list(items)

    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove an element from the top of a stack and return it"""
        return self.items.pop()

    def peek(self):
        """Return the element at the top of stack without removing it"""
        if len(self.items) == 0:
            return 'Stack is empty'
        return self.items[-1]

    def size(self):
        """Count the number of elements in the stack"""
        return len(self.items)

    def is_empty(self):
        """bool: True if stack is empty False otherwise"""
        return len(self.items) == 0

    def __repr__(self):
        items = ", ".join([str(item) for item in self.items])
        return f'Stack({items})'


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(1, 2, 3)
        self.empty_stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(str(self.stack), 'Stack(1, 2, 3, 1)')

    def test_pop(self):
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, 3)
        self.assertEqual(str(self.stack), 'Stack(1, 2)')

    def test_peek(self):
        peeked_item = self.stack.peek()
        self.assertEqual(peeked_item, 3)
        self.assertEqual(str(self.stack), 'Stack(1, 2, 3)')
        self.assertEqual(self.empty_stack.peek(), 'Stack is empty')

    def test_size(self):
        self.assertEqual(self.stack.size(), 3)

    def test_empty(self):
        self.assertTrue(self.empty_stack.is_empty())
        self.assertFalse(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()

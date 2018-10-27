import unittest

class Queue:
    """Python implementation of a queue using python list
    (without using collections module)
    can use collections.deque to implement queue 
    with a more efficienct dequeue method"""

    def __init__(self, *items):
        self.items = list(items)
    
    def enqueue(self, ele):
        """Add element to the rear (right) of your Queue"""
        self.items.append(ele)
    
    def dequeue(self):
        """Remove element from the front (left) of your Queue"""
        return self.items.pop(0)
    
    def is_empty(self):
        """Returns True if Queue is empty False otherwise"""
        return len(self.items) == 0

    def __repr__(self):
        items = ", ".join([str(item) for item in self.items])
        return f'Queue({items})'


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(1,2,3)
        self.empty_queue = Queue()
    
    def test_enqueue(self):
        self.queue.enqueue(4)
        self.assertEqual(str(self.queue), 'Queue(1, 2, 3, 4)')
    
    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 1)

    def test_empty(self):
        self.assertFalse(self.queue.is_empty())
        self.assertTrue(self.empty_queue.is_empty())
    

if __name__ == '__main__':
    unittest.main()
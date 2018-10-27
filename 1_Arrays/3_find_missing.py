import unittest


def finder(arr1, arr2):
    """ Given 2 arrays find which element from the first
    array is missing from the second array
    (you can have duplicate numbers)
    i.e: 
    >>> finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) 
    '5 is the missing number'
    """
    count = {}
    for n in arr1:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    for n in arr2:
        count[n] -= 1
    for num in count:
        if count[num] == 1:
            return f'{num} is the missing number'


def finder2(arr1, arr2):
    count = 0
    for n in arr1:
        count += n
    for n in arr2:
        count -= n
    return f'{count} is the missing number'


class TestSolution(unittest.TestCase):
    def test(self):
        sol = finder
        self.assertEqual(sol([1, 2, 3], [2, 3]),
                         "1 is the missing number")
        self.assertEqual(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]),
                         "5 is the missing number")
        self.assertEqual(sol([5, 5, 7], [5, 7]),
                         "5 is the missing number")


if __name__ == '__main__':
    unittest.main()

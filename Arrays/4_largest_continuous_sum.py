import unittest

def large_cont_sum(arr):
    """Given an array of integers (positive and negative)
    return the slice of the largest continous sum  and sum itself"""
    if len(arr) == 0:
        return 'Empty Array: No values to sum'
    
    start = curr_start = 0 
    end = curr_end = 1
    max_sum = current_sum = arr[0]

    for index, num in enumerate(arr[1:], 1):
        #Keep track of current sum and start and end of current slice
        if current_sum + num < num:
            curr_start = index
            curr_end = curr_start + 1
            current_sum = num
        else:
            curr_end += 1
            current_sum += num
        
        #compare current_sum with max_sum update if max_sum if needed
        if max_sum < current_sum:
            start = curr_start
            end = curr_end
            max_sum = current_sum
    
    return arr[start:end], max_sum

class TestSolution(unittest.TestCase):
    def test(self):
        sol = large_cont_sum
        self.assertEqual(sol([1, 2, -1, 3, 4, -1]), ([1, 2, -1, 3, 4], 9))
        self.assertEqual(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 
                        ([1, 2, -1, 3, 4, 10, 10], 29))
        self.assertEqual(sol([-1, 1]), ([1], 1))


if __name__ == '__main__':
    unittest.main()

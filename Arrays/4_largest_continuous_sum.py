import unittest

def large_cont_sum(arr):
    """Given an array of integers (positive and negative)
    return the largest continuous sum"""
    """
    1. initialize the max_sum and current_sum as the first element
    2. loop through the rest of the nums of arr
    3. compare each num with the current_sum + num
    4. if current_sum + num is less than num itself current_sum is num
    5. max sum is the max of max_sum and current_sum"""
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        if num > current_sum + num:
            current_sum = num
        else:
            current_sum += num

        max_sum = max(max_sum, current_sum)

    return max_sum

class TestSolution(unittest.TestCase):
    def test(self):
        sol = large_cont_sum
        self.assertEqual(sol([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(sol([-1, 1]), 1)


if __name__ == '__main__':
    unittest.main()

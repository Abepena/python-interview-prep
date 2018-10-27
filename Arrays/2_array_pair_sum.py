import unittest


def array_pair_sum(arr, k):
    """ Given an array of integers and target k
    return all unique pairs that add up to k
    Ex:
    >>> array_pair_sum([1,3,2,2],4)
    [(1,3),(2,2)]
    """
    lookup = set()
    output = set()
    for num in arr:
        target = k - num
        if target in lookup:
            output.add((target, num))
        else:
            lookup.add(num)

    return "\n".join([str(tup) for tup in output])


print(array_pair_sum([1, 3, 2, 2], 4))


class TestArrayPairSum(unittest.TestCase):
    def test(self):
        sol = array_pair_sum
        self.assertEqual(sol([1, 3, 2, 2, 1, 3], 4),
                         "(1, 3)\n(2, 2)")


if __name__ == "__main__":
    unittest.main()
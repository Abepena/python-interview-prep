import unittest


def unique(s):
    """Check if all characters in a string are unique
    :type s: input string of characters
    :rtype: bool
    """
    return len(set(s)) == len(s)

def unique2(s):
    seen = set()
    for letter in s:
        if letter in seen:
            return False
        else:
            seen.add(letter)
    return True


class TestSolution(unittest.TestCase):
    def test(self):
        sol = unique2
        self.assertFalse(sol('aaabbb'))
        self.assertTrue(sol('abcdefg'))


if __name__ == '__main__':
    unittest.main()

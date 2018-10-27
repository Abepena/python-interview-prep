import unittest

def compress(s):
    """ :type s: str - uppercase/lowercase letters
    :rtype: str - letters followed by count
    ex:
    >>> compress('AAABBB')
    'A3B3'
    """
    current_letter = s[0]
    count = 1
    output = ''
    for letter in s[1:]:
        if letter == current_letter:
            count += 1
        else:
            output += current_letter + str(count)
            current_letter = letter
            count = 1
    output += current_letter + str(count)
    return output



class TestSolution(unittest.TestCase):
    def test(self):
        sol = compress
        self.assertEqual(sol('AAABBBCCCCCDDEE'), 'A3B3C5D2E2')
        self.assertEqual(sol('AAAaaaBBBbbb'), 'A3a3B3b3')

if __name__ == '__main__':
    unittest.main()
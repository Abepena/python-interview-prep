import unittest


def anagram(s1, s2):
    """Check that two strings are anagrams of each other
    Ignore spaces and not case sensitive"""
    s1 = s1.replace(" ", '').lower()
    s2 = s2.replace(" ", '').lower()
    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    """Without using sorted
    1. Lower and remove spaces from both strings
    2. Map the letters from the first string to a count dict
    3. Remove the letters from the second string from the count dict
    4. If you have any key in the count dict not 0 return False else True"""
    
    # 1
    s1 = s1.replace(" ", '').lower()
    s2 = s2.replace(" ", '').lower()
    count = {}

    # 2
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # 3
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False
    
    for num in count.values():
        if num != 0:
            return False

    return True



class ArrayTests(unittest.TestCase):
    def test_anagram_check(self):
        #change sol between anagram/anagram2
        sol = anagram2
        self.assertEqual(sol('go go go', 'gggooo'), True)
        self.assertEqual(sol('abc', 'cba'), True)
        self.assertEqual(sol('hi man', 'hi     man'), True)
        self.assertEqual(sol('aabbcc', 'aabbc'), False)
        self.assertEqual(sol('123', '1 2'), False)


if __name__ == "__main__":
    unittest.main()

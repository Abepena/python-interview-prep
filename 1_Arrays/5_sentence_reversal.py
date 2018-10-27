import unittest


def reverse_sentence(s):
    """Reverse the words in a phrase/sentence
    Sentences can have leading and trailing whitespace and
    words are seperated by 1 space"""
    return " ".join(s.split()[::-1])


class TestSolution(unittest.TestCase):
    def test(self):
        sol = reverse_sentence
        self.assertEqual(sol('This is the best'), 'best the is This')
        self.assertEqual(sol('     hello world   '), 'world hello')


if __name__ == '__main__':
    unittest.main()

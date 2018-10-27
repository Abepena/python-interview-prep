import unittest

def balance_paren(parens):
    """Given a string of opening and closing brackets
    Return a boolean of whether the Parentheses are balanced or not

    {}[]() --> True | {[{]}} --> False
    {[()]} --> True | [{}    --> False
    [{}()] --> True | }      --> False
    """
    #return early if we had odd # of brackets
    if len(parens) % 2 != 0:
        return False

    pairs = set([('[',']'),('(',')'),('{','}')])
    opening = set(['{','(','['])
    stack = []

    for paren in parens:
        # add to stack if we have an opening bracket
        if paren in opening:
            stack.append(paren)
        else:
            #check that we have an opening bracket in stack
            #otherwise return early
            if stack:
                last_open = stack.pop()
                #check that the last opening bracket seen is
                # the current brackets pair
                if (last_open, paren) not in pairs:
                    return False
            else:
                return False
    
    #True if stack is empty after balancing the brackets
    return len(stack) == 0 


class TestSolution(unittest.TestCase):
    def test(self):
        sol = balance_paren
        self.assertTrue(sol('{}[]()'))
        self.assertTrue(sol('{[()]}'))
        self.assertTrue(sol('[{}()]'))
        self.assertFalse(sol('[{}'))
        self.assertFalse(sol('{[{]}}'))
        self.assertFalse(sol('{{{{'))


if __name__ == '__main__':
    unittest.main()
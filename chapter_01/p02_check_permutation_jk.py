import unittest
from collections import Counter
def check_permutation_jk(s1,s2):
    # same length
    if len(s1) != len(s2):
        return False
    # same count (histogram) of chars
    return Counter(s1) == Counter(s2)

if __name__ == '__main__':
    s1 = "abc"
    s2 = "cba"
    print(check_permutation_jk(s1,s2))
class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_jk
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation_jk(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
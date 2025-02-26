import time
import unittest


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)



#aabccccaaa - > a2b1c4a3
#abbb
#a
def string_compression(s):
    compress = []
    counter = 0
    can_compress = False
    print(s)
    for i in range(len(s)):
        if i != 0 and (s[i] != s[i-1]): # Has previous and current does not match previous
            compress.append(s[i-1])
            compress.append(str(counter))
            counter = 0
        counter += 1
    # append last match
    if counter:
        compress.append(s[-1])
        compress.append(str(counter))

    # returns original string if compressed string isn't smaller
    return min(s, "".join(compress), key=len)












class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,string_compression
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()

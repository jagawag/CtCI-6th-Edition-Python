import string
from collections import Counter
import string
#aabbc -> abcba
#aabb -> abba
#dddeee -> dd
def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]

# Create char count dictionary (Counter). Iterate over count.values(). If more than 1 odd, return False.
def palindrome_perm(s):
    word = clean_phrase(s)
    counts = Counter(word)
    mid = False # assume even length
    for v in counts.values():
        odd = v % 2 != 0
        if odd:
            if not mid: # found potential middle value
                mid = True
            else: # found second char with odd count. Can't have two middles.
                return False
    return True

if __name__ == "__main__":
    print(palindrome_perm("taco cat"))

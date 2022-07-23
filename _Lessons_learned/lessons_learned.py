"""Tips"""
import string

top = "\n-----------\n"
bottom = "\n-----------"

print(f"{top}Random Tips{bottom}")
dir(list) # returns object model. All callable functions.
help('keywords') # returns info from help menu (modules, keywords, or used empty help())


print("Chapter 1")
print(f"{top}Unique character count{bottom}")
str1 = "abcc"
print(len(set(str1))) # returns 3
print(f"{top}Is Permutation{bottom}")
"""Counter from collections is a subclass of Dictionary and creates a histogram."""
from collections import Counter
histogram = Counter([1,2,3,4,5,4,3,2,3,3])
histogram2 = Counter([1,2,])

print(histogram[3]) # returns value (count) at key 3
print(histogram.most_common(1)) # returns most common item as tuple in new list
print(histogram.most_common()[0]) # returns most common tuple
print(histogram + histogram2)
print(histogram & histogram2)
print(histogram | histogram2)


print(f"{top}Permutation Palindrone{bottom}")
# Create char count dictionary (Counter). Iterate over hist.values(). If more than 1 odd, return False.
print(string.ascii_lowercase)

print(f"{top}One Away{bottom}")
# Given two strings, can you make them match by performing exactly 1 add, delete, or edit?
lessons ={"Add/Delete are the same depending on the reference string",
          "Performing skip one comparisons can be done with nested forloops using range"}
print(f"Key lessons: {lessons}")

print(f"{top}String Compression{bottom}")

print(f"{top}Rotate Matrix{bottom}")
print("NEED TO REVIEW and practice")

link = "https://realpython.com/operator-function-overloading/"
print(f"Reread on special functions and operator overloading: {link}")

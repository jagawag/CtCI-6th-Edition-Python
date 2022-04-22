'''Determine if a string has all unique chars.
What if you can't use additional data structures?'''

s = "some long"
unique = True
for i in range(len(s)):
    if s[i] in s[i+1:]:
        unique = False
        break
    print(s[i])
print(unique)
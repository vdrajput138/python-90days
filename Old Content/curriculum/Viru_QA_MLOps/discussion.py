"""
Get string from user.
make a loop of all alphabets
add unique alphabets in an array
if found duplicate, create an entry if not found in dict and increament the count.

aabbccddddeerrdd
a -2
b -2
d - 4



{"a": 1}, {"b":1}


inputString = input("Enter a string")
uniqueArray = []
commonAlphabets = {}

for alphabet in inputString:
    print(alphabet)
    if len(uniqueArray) == 0 or alphabet not in uniqueArray:
        uniqueArray.append(alphabet)
    else:
        if alphabet in commonAlphabets:
            val = commonAlphabets.get(alphabet)
            val = val +1
            commonAlphabets[alphabet] = val
        else:
            commonAlphabets[alphabet] = 2

print(uniqueArray)
print(commonAlphabets)
"""

from collections import Counter

s = input("Enter a string: ")

unique_chars = list(dict.fromkeys(s))  # preserves order
freq = Counter(s)

common = {k: v for k, v in freq.items()}

print(unique_chars)
print(common)
print(freq)

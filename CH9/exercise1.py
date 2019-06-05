# Write a program that reads the words inwords.txtand stores them askeys in a dictionary. It doesn’t matter what the values are. Then youcan use theinoperator as a fast way to check whether a string is in thedictionary.

from collections import defaultdict

f = input("Enter file name: ")
try:
    content = open(f)
except:
    print("File no good", f)
    quit()

counts = defaultdict(lambda: 0)
# counts = dict()
for line in content:
    words = line.split()
    for word in words:
        counts[word] += 1
        # counts[word] = counts.get(word,0) + 1

def check_existance(word):
    if word in counts:
        print(f'Found it {counts[word]} times!')
    else:
        print("Didn't see it")

word_to_find = input("Look for your word: ")
check_existance(word_to_find)
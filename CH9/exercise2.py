from collections import defaultdict

f = input("Enter file name: ")
try:
    content = open(f)
except:
    print("File no good", f)
    quit()

counts = dict()
for line in content:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    for word in words:
        target = words[2]
    counts[target] = counts.get(target, 0) + 1

print(counts)
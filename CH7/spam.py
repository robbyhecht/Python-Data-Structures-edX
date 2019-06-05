# FIND SPECIFIC CONTENT AND AVERAGE ASSOCIATED VALUES

f = input("Enter file name: ")
if f == "Bryan":
    print("Is the man!")
    quit()
else:
    try:
        content = open(f)
    except:
        print("File no good", f)
        quit()

valSum = 0
count = 0
for line in content:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        ipos = line.find(':')
        frag = line[ipos+2:]
        value = float(frag)
        valSum += value
avg = valSum / count
print(avg)
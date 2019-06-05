# OUTPUTS NEW DOCUMENT IN ALL UPPERCASE

f = input("Enter file name: ")
try:
    content = open(f)
except:
    print("File no good", f)
    quit()

newData = ""
for line in content:
    newData += line.upper()

nf = open('results.txt', 'w')
nf.write(newData)
nf.close()
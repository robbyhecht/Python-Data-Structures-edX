name = input("Enter file:")
if len(name) < 1 : name = "file.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.rstrip() #remove whitespace
    if not line.startswith("From ") or len(line) < 3: continue # remove superfluous lines
    words = line.split() # split lines into words (otherwise the index will refer to one giant string)
    emails = words[1] # grab only the emails by their index of 1
    di[emails] = di.get(emails, 0) + 1 # idiom: retrieve/create/update counter

# the counter is now the value in the key/value pairs-- find the most common email using the values

largest = -1 # existing keys will have a positive count, so this acts as a valid boolean for counter
theword = None # counter for keys
for k,v in di.items(): # .items gives key/value pairs
    if v > largest:
        largest = v # capture/remember the value that was largest
        theword = k # capture/remember the key that was largest
print(theword, largest)


# ----
        # oldcount = di.get(word, 0)
        # newcount = oldcount + 1
        # di[word] = newcount

        # IS SAME AS:

        # di[word] = di.get(word, 0) + 1
# ----
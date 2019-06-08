name = input("Enter file:")
if len(name) < 1 : name = "file.txt"
handle = open(name)

dic = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") or len(line) < 3: continue
    words = line.split()
    times = words[5]
    times = times.split(":")
    hours = times[0]
    dic[hours] = dic.get(hours, 0) + 1
dic = sorted(dic.items())
for k,v in dic:
	print(k,v)
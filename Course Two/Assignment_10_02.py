name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

fh = open(name)

counts = dict()
lst = list()

for line in fh:
    ly = line.rstrip()
    words = line.split()
    if ly.startswith("From "):
        hour = words[5]
        lst.append(hour[0:2])

for key in lst:
    counts[key] = counts.get(key, 0) + 1

sorted_counts = sorted(counts)

for key in sorted_counts:
    print(key, counts[key])

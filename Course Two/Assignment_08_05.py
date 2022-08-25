fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    ly = line.rstrip()
    words = line.split()
    if ly.startswith("From "):
        count = count + 1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")

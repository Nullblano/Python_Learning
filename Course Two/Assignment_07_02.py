# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File cannot be opened or does not exist:", fname)
    exit()

count = 0
total = 0

for line in fh:
    ly = line.rstrip()
    if not ly.startswith("X-DSPAM-Confidence:"):
        continue
    total = total + float(ly[-6:])
    if ly.startswith("X-DSPAM-Confidence:"):
        count = count + 1

print("Average spam confidence:", total/count)

import re

name = input("Enter file:")
if len(name) < 1:
    name = "actual.txt"
handle = open(name)

sum = 0

reading_file = handle.read()
finding_numbers = re.findall('([0-9]+)', reading_file)

for changing_to_int in range(0, len(finding_numbers)):
    finding_numbers[changing_to_int] = int(finding_numbers[changing_to_int])
    sum += finding_numbers[changing_to_int]

print(sum)

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        inp = int(num)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None:
        largest = inp
        smallest = inp

    if inp > largest:
        largest = inp
    if inp < smallest:
        smallest = inp

print("Maximum is", largest)
print("Minimum is", smallest)

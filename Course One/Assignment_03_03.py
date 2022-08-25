
# take out breaks to keep user input loop going

while True:
    score = float(input("Enter Score: "))

    if 0.9 <= score <= 1.0:
        print('A')
        # break
    elif 0.8 <= score < 0.9:
        print('B')
        # break
    elif 0.7 <= score < 0.8:
        print('C')
        # break
    elif 0.6 <= score < 0.7:
        print('D')
        # break
    elif 0.0 <= score < 0.6:
        print('F')
        # break
    else:
        print("Bad Score. Please try again.")

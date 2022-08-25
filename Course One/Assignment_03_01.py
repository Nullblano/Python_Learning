hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    overtime = (h-40)*(r*1.5)
    standard = 40
    pay = overtime + (standard*r)
    print(float(pay))
else:
    print(h*r)

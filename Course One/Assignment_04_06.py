def computepay(hours, rates):
    if hours > 40:
        standard = 40
        overtime = (hours-40)*(rates*1.5)
        pay = overtime + (standard*rates)
        return pay
    else:
        pay = hours * rates
        return pay


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

xp = computepay(h, r)
print("Pay", xp)




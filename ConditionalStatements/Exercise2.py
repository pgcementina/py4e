
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40 * rate
else:
    pay = hours * rate

print("Pay: ", pay)

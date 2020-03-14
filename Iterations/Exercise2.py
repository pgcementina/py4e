count = 0

while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue

    if count == 0:
        min_val = fval
        max_val = fval
    elif fval < min_val:
        min_val = fval
    elif fval > max_val:
        max_val = fval

    count = count + 1


print('Minimum Value:', min_val, 'Maximum Value:', max_val)

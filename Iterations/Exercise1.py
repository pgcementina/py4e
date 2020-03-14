count = 0
total = 0

while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    total = total + fval
    count = count + 1

print('Total:',total,'Count:', count,'Average:', total/count)

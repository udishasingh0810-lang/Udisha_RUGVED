num = input("Enter a number: ")

digits = [int(d) for d in num]

peak = 0

while peak < len(digits) - 1 and digits[peak] < digits[peak + 1]:
    peak += 1

if peak == 0 or peak == len(digits) - 1:
    print("Not a hill number")
else:
    is_hill = True

    for i in range(peak, len(digits) - 1):
        if digits[i] <= digits[i + 1]:
            is_hill = False
            break

    if is_hill:
        print("Hill number")
    else:
        print("Not a hill number")
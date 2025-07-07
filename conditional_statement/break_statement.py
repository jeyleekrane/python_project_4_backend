# this block of code breaks the conditiononce some certain condiotions are reached

number = 6

while number > 0:
    number = number-1
    if number == 3:
        break
    print(f"{number}")

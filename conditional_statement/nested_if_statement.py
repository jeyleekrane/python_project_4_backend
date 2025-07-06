# lets make a user to enter a random number n check the number using a nested if statement

number = float(
    input("Please enter any random number please not a float number: "))
if number > 10:
    if number == 12:
        print("the number u entered is 2")
    elif number == 14:
        print("the number u entered id exactly 4")
    elif 10 < number < 120:
        print("10 is les than number and 120 ")
    else:
        print("u have entered a number with a decimal point")
else:
    print("not in range")

# in this code a user will be assked to enter a number wile we randomly generate a multication table
number = int(input(
    "Please enter an integer number while we generate a muliplication table for you  =  "))
counter = 1
while counter <= 12:
    print(f"{number} * {counter} =" + f"{number*counter}")
    counter = counter+1

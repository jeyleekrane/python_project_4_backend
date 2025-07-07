# A SIMPLE PRIME NUMBER PYHON STUFF know that a prime number is a number only divible by it sef
number = int(
    input("please any number so we know if its a prime number of not = "))

print(number)
if (number % 2 != 0):
    print(f"{number} is a a prime number")
else:
    print(f"{number} is a not a prime number")

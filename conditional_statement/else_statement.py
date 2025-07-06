# simple else statement

Account_Balance = 200000.00

Amount_withdraw = float(
    input("please enter the amount of money u want to withdraw: "))

if Amount_withdraw > Account_Balance:
    print("the amount of money u want to withdraw is not aviailable in your account")
else:
    print("please insert your pin: ")

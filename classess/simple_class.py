class UserProfile:
    def __init__(self, username, password, email_address):
        self.username = username
        self.password = password
        self.email_address = email_address

    def welcome_message(self):
        return f"The username yoou entered is {self.username} , your password is {self.password} and your email address is {self.email_address}"


user1 = UserProfile("jeyleekrane", "please let me in",
                    "ijeyleekrane@gmail.com")

print(user1.welcome_message())


class Customer(UserProfile):
    def __init__(self, username, password, email_address):
        self.username = username
        self.password = password
        self.email_address = email_address
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def a_customer_greetings(self):
        return f"The username yoou entered is {self.username} , your password is {self.password},your email address is {self.email_address}, and you owe {self.balance} "


user12 = Customer("jeyleekrane", "12wddufheuf", "ijeyleekrane@gmail.com")
user12.set_balance(200)

print(user12.a_customer_greetings())

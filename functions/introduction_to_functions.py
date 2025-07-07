def password_harshing(password, passkey, pass_phress):
    keyharshed = pass_phress+passkey+password

    return keyharshed


Dfunction = password_harshing(2, 1, 2)
print(Dfunction)


def clear_user_name(username1, *password1):
    password_keeper = username1 + password1
    return password_keeper


founder = clear_user_name(2, 3, 1)

print(founder)

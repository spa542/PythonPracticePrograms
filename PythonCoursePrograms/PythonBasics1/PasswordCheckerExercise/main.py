username = input('Enter username: ')
password = input('Enter password: ')

passwordLength = len(password)
hidden_password = '*' * passwordLength
print(f'{username}, your password {hidden_password}, is {passwordLength} letters long')

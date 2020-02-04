data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
# In this task, we will try to verify if the user enters a password
# that belongs to his account.

choice_username = input('Enter username pls.: ')

ok_pass = data.get(choice_username)

if not ok_pass:
    print('Username not found!')
    quit()

choice_password = input('Enter your password: ')

if choice_password == ok_pass:
    print('Welcome')
else:print('Username or password is wrong!')
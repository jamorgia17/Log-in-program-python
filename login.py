userName = 'Angelo'
userPassword = 'Password123'
attempt = 0

while attempt < 3:
    enteredName = input('Enter your username: ')
    enteredPassword = input('Enter your password: ')
    attempt += 1
    
    if enteredName == userName and enteredPassword == userPassword:
        print('Welcome back, Angelo!')
        break
    elif enteredName == userName and enteredPassword != userPassword:
        print('Hi, Angelo! I think you have entered the wrong password.')
    elif enteredName != userName and enteredPassword != userPassword:
        print('I do not know you, HACKER')
    else:
        print('Please do not destroy my program')

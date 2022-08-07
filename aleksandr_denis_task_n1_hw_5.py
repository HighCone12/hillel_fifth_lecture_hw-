password = 132
password1: int = int(input('Enter your password'))
while True:
    if password1 == password:
        print(f'Welcome!')
        break
    else:
        print('Please, enter it again')
        break


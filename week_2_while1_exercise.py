def hello_user():
    while True:
        ask = input("Как дела? \n")
        if ask == 'Хорошо':
            print('Круто')
            break
    hello_user()
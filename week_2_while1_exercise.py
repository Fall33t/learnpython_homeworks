def hello_user():
    while True:
        ask = input("Как дела? \n")
        if ask == 'Хорошо':
            print('Круто')
            break
if __name__ == "__hello_user__":
    hello_user()
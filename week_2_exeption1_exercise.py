def hello_user():
    try:
        while True:
            user_say = input("Как дела? \n")
            if user_say == "Хорошо":
                print("Круто")
                break
    except KeyboardInterrupt:
        print("Пока!")
if __name__ == "__hello_user__":
    hello_user()



def ask_user():
    ask = input("Спроси меня \n")
    ask_answ = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        if ask in ask_answ:
            print(ask_answ[ask])
            break
if __name__ == "__ask_user__":
    ask_user()



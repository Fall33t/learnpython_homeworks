def ask_user():
    ask = input("Спроси меня \n")
    ask_answ = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        if ask in ask_answ:
            print(ask_answ[ask])
            break
    ask_user()



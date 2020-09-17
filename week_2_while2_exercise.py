ask = input("Спроси меня")
ask_answ = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
while True:
    if ask == ask_answ["Как дела?"]:
        print(ask_answ["Как дела?"])
    if ask == ask_answ["Что делаешь?"]:
        print(ask_answ["Что делаешь?"])
        break



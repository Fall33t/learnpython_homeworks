def main(one = input("Число строка1 \n"), two = input("Число строка2 \n")):
    if one != str(one) or two != str(two):
        return print(0)
    elif one == two:
        return print(1)
    elif len(one) > len(two):
        return print(2)
    elif two == "learn":
        return print(3)
    main()
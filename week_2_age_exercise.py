def main(user_age = int(input("Укажите свой возраст \n"))):
   if 3 < user_age <= 6:
       return print('Вы должны ходить в детский сад!')
   elif 6 < user_age <= 17:
       return print('Вы должны ходить в школу!')
   elif 17 < user_age <= 23:
       return print('Вы должны учиться в университете!')
   elif 23 < user_age <= 65:
       return print('Вы должны работать!')
   else:
       return print('Вы пенсионер')
if __name__ == "__main__":
   main()
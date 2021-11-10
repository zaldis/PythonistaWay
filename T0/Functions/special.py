# # Если функция ничего не возвращает явно, то она вернет тип None
def do_something():
    5 + 6  # этого не будет в result, та как нет слова return


result = do_something()  # None
print(result)


def say_hello():
    print('hello')


# если не указать ()
# то в переменную положим саму функцию, а не ее результат
micro = say_hello
micro()


# # для тех, кто уже знаком с понятием Python объектов
say_hello.tag = 'sayer'
print(say_hello.__dict__, say_hello.tag)

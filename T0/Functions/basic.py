def heat_water(water, pot, steve, temperature):
    """
    Создать функцию для нагрева воды

    Принимает:
        - воду
        - кастрюлю
        - плита
        - температуру

    Возвращает:
        - нагретую воду
    """
    # нагреваем воду <water> в кастрюле <pot> на плите <steve> до температуры <temperature>
    warm_water = ...
    return warm_water


def is_triangle_exists(a, b, c):
    """
    Создать функцию проверки существования трeугольника

    Принимает:
        a, b, c - стороны треугольника

    Возвращает:
        True - если треугольник с такими сторонами существует
        False - ... не существует
    """
    is_exists = (a + b > c) and (a + c > b) and (b + c > a)
    return is_exists


print(is_triangle_exists(10, 12, 21))

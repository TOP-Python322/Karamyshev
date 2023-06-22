def orth_triangle(
        *,
        cathetus1: float = None,
        cathetus2: float = None,
        hypotenuse: float = None
# ИСПРАВИТЬ: аннотировать возможность функции вернуть объект None
) -> float:
    # ДОБАВИТЬ: строку документации
    if cathetus1 is not None and cathetus2 is not None:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    elif cathetus1 is not None and hypotenuse is not None:
        # ИСПРАВИТЬ: эту и аналогичные проверки — с одинаковым результатом — лучше проводить независимо в самом начале выполнения функции
        if cathetus1 > hypotenuse:
            return None
        return (hypotenuse ** 2 - cathetus1 ** 2) ** 0.5
    elif cathetus2 is not None and hypotenuse is not None:
        if cathetus2 > hypotenuse:
            return None
        return (hypotenuse ** 2 - cathetus2 ** 2) ** 0.5
    # ИСПРАВИТЬ: этот блок сработает только в случае передачи недостаточного количества аргументов, а в случае передачи избыточного количества — не сработает (см. пример ниже)
    else:
        return None


# >>> print(orth_triangle(cathetus1=3, cathetus2=4, hypotenuse=5))
# КОММЕНТАРИЙ: а должно быть None
# 5.0


# СДЕЛАТЬ: выполнить проверку работоспособности функции согласно требованиями задания
# ДОБАВИТЬ: комментарий с результатами проверки со своими входными данными


# ИТОГ: неплохо, но нужно лучше — 3/6

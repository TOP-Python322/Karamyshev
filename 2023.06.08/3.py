# ИСПОЛЬЗОВАТЬ: длинные списки параметров (особенно с аннотациями) записывают вертикально
def numbers_strip(
        numbers: list[float],
        n: int = 1,
        return_copy: bool = False
) -> list[float]:
    # ДОБАВИТЬ: строку документации
    if return_copy:
        numbers = numbers.copy()

    for _ in range(n):
        if numbers:
            numbers.remove(min(numbers))
            numbers.remove(max(numbers))

    return numbers


# СДЕЛАТЬ: выполнить проверку работоспособности функции согласно требованиями задания
# ДОБАВИТЬ: комментарий с результатами проверки со своими входными данными


# ИТОГ: код хороший, доработать задачу целиком — 3/5

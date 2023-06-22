def central_tendency(num1: float, num2: float, *numbers: float) -> dict[str, float]:
    # ДОБАВИТЬ: строку документации

    # ИСПРАВИТЬ: переменные numbers и all_numbers используются только по разу, в их создании нет необходимости — следует перезаписать переменную numbers отсортированным списком всех чисел
    all_numbers = [num1, num2, *numbers]
    sorted_numbers = sorted(all_numbers)
    length = len(sorted_numbers)

    if length % 2 == 0:
        median = (sorted_numbers[length//2-1] + sorted_numbers[length//2]) / 2
    else:
        median = sorted_numbers[length//2]

    arithmetic_mean = sum(sorted_numbers) / length
    geometric_mean = 1
    for number in sorted_numbers:
        geometric_mean *= number
    geometric_mean = geometric_mean ** (1 / length)
    harmonic_mean = length / sum(1 / number for number in sorted_numbers)

    return {
        'median': median,
        'arithmetic': arithmetic_mean,
        'geometric': geometric_mean,
        'harmonic': harmonic_mean
    }


# СДЕЛАТЬ: выполнить проверку работоспособности функции согласно требованиями задания
# ДОБАВИТЬ: комментарий с результатами проверки со своими входными данными


# ИТОГ: хорошо, доработать — 3/5

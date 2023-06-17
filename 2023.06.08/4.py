def countable_nouns(number: int, options: tuple[str, str, str]) -> str:
    last_digit = number % 10
    last_two_digits = number % 100

    if last_digit == 1 and last_two_digits != 11:
        return options[0]
    elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
        return options[1]
    else:
        return options[2]

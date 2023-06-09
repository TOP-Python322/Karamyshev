# ИСПОЛЬЗОВАТЬ: согласно PEP 8, комментарий следует располагать над комментируемой строчкой кода
# making a function with object "password" which will use as main object
# ДОБАВИТЬ: аннотации типов параметров и возвращаемого объекта
def strong_password(password):
    # ДОБАВИТЬ: строку документации
    # make sure it length not less than 8
    if len(password) < 8:
        # if it so return False
        return False

    # making a list of flags which shall help us rightr mark making
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_chars = False

    for char in password:
        # if it contain just any lower char
        if char.islower():
            has_lowercase = True
        # if it contain just any upper char
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            # ИСПРАВИТЬ: внимательнее читайте задание: в условии есть требование о том, что цифр в пароле должны быть минимум две (см. пример выполнения вашего кода ниже)
            has_digit = True
        # if it contain just other sort of chars
        else:
            has_special_chars = True

    # if any conditions satisfy we return True for all has_* flags
    return has_lowercase and has_uppercase and has_digit and has_special_chars


# >>> strong_password('ABcdef!1')
# КОММЕНТАРИЙ: а должно быть False
# True

# СДЕЛАТЬ: прочитайте внимательно окончание текста задания — там описано, как именно следует проверять свой код

# ДОБАВИТЬ: результаты проверки со своими входными данными должны быть скопированы и в закомментированном виде добавлены в конец файла с кодом (см. пример выше)

# КОММЕНТАРИЙ: эти требования являются обязательной частью каждой задачи


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/


# ИТОГ: код неплохой, однако, требуется доработать — 3/6

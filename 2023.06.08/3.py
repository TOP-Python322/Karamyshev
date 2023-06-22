# ИСПОЛЬЗОВАТЬ: длинные списки параметров (особенно с аннотациями) записывают вертикально
def numbers_strip(
        numbers: list[float],
        n: int = 1,
        return_copy: bool = False
) -> list[float]:
    if return_copy:
        numbers = numbers.copy()

    for _ in range(n):
        if numbers:
            numbers.remove(min(numbers))
            numbers.remove(max(numbers))
    
    return numbers



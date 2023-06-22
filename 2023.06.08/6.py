def orth_triangle(
        *, cathetus1: float = None,
        cathetus2: float = None,
        hypotenuse: float = None
) -> float:
    if cathetus1 is not None and cathetus2 is not None:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    elif cathetus1 is not None and hypotenuse is not None:
        if cathetus1 > hypotenuse:
            return None
        return (hypotenuse ** 2 - cathetus1 ** 2) ** 0.5
    elif cathetus2 is not None and hypotenuse is not None:
        if cathetus2 > hypotenuse:
            return None
        return (hypotenuse ** 2 - cathetus2 ** 2) ** 0.5
    else:
        return None



from math import log, e


def log_10(val: int) -> float:
    return log_10(val)


def ln(val: int) -> float:
    return log(val, e)


def factorial(val: int) -> int:
    if val == 1:
        return 1
    
    return factorial(val - 1) * val

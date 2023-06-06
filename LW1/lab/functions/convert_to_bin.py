from lab.functions.convert import *


def convert_straight(x: int) -> str:
    sign = "0" if x >= 0 else "1"
    binary = convert(abs(x)).zfill(BIT-1)
    return sign + binary


def convert_reverse(x: int) -> str:
    sign = "0" if x >= 0 else "1"
    binary = convert(abs(x)).zfill(BIT-1)
    if sign == "1":
        binary = "".join(["1" if bit == "0" else "0" for bit in binary])
    return sign + binary


def convert_additional(x: int) -> str:
    result = convert(x)
    if x == 0:
        result = "0" * BIT
    elif x >= 0:
        result = "0" + result
    if x < 0:
        result = convert_reverse(x)
        total = list(result)
        for i in range(len(total) - 1, -1, -1):
            if total[i] == "0":
                total[i] = "1"
                break
            if total[i] == "1":
                total[i] = "0"
        result = "".join(total)

    return result

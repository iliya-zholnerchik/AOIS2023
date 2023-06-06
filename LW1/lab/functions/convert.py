from lab.settings import *


def convert(number: int) -> str:
    result = ""
    number = abs(number)
    while number > 0:
        y = str(number % 2)
        result = y + result
        number = int(number / 2)

    add = BIT - (len(result) + 1)
    result = add * "0" + result

    return result


def convert_ten(x: str) -> int:
    total = 0
    step = 0
    for i in range(len(x) - 1, 0, -1):
        if x[i] == "1":
            total += pow(2, step)
        step += 1
    if x[0] == "0":
        return total
    else:
        return int("-" + str(total))

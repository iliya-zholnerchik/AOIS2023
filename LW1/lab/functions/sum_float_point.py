from lab.functions.sum import *
from lab.functions.convert_to_bin import *


def float_to_bin(num: str) -> tuple:
    integer, float_1 = num.split('.')
    fraction = abs(float(num) - int(integer))
    result = ''
    integer = convert_straight(int(integer))
    integer = integer[integer.find('1') - 1:]
    index = -1
    while fraction > 0:
        if fraction - pow(2, index) >= 0:
            result += '1'
            fraction -= pow(2, index)
        else:
            result += '0'
        index -= 1

    return integer, result


def sum_float(num_1, num_2) -> str:
    num_1_copy, num_2_copy = num_1, num_2
    num_1_int, num_1_fl = float_to_bin(num_1)
    num_2_int, num_2_fl = float_to_bin(num_2)
    max_fl, max_int = max(len(num_1_fl), len(num_2_fl)), max(len(num_1_int), len(num_2_int))
    num_1_fl, num_2_fl = num_1_fl + (max_fl - len(num_1_fl)) * '0', num_2_fl + (max_fl - len(num_2_fl)) * '0'
    num_1_int, num_2_int = (max_int - len(num_1_int)) * '0' + num_1_int, (max_int - len(num_2_int)) * '0' + num_2_int
    num_1, num_2 = num_1_int + num_1_fl, num_2_int + num_2_fl
    result = sum_additional(convert_additional(convert_ten(num_1)),
                            convert_additional(convert_ten(num_2)))
    answer = ''.join(result[:-max_fl]) + ',' + ''.join(result[-max_fl:])
    index = convert(max_fl)
    if float(num_1) + float(num_2) > 0:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{num_1_copy} + {num_2_copy} = {bin_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'
    else:
        print(f'{result[0]}.{result[result.find("1", 1):]}*2^1.{index[index.find("1"):]}')
        return f'{num_1_copy} + {num_2_copy} = {bin_to_float(answer)} = {answer[0]}.{answer[answer.find("1", 1):]}'


def bin_to_float(num: str) -> float:
    integer, float_1 = num.split(',')
    integer = convert_ten(integer)
    total = integer
    index = -1
    for i in range(0, len(float_1)):
        if float_1[i] == "1":
            total += pow(2, index)
        index -= 1
    return total

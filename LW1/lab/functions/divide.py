from lab.functions.convert_to_bin import *
from lab.functions.sum import *
from lab.settings import *


def divide(numerator: str, denominator: str) -> str:
    integer = "".join(ZERO)
    flag = numerator[0] != denominator[0]
    numerator = '0' + numerator[1:]
    denominator = '1' + denominator[1:]
    additional_numerator = convert_additional(convert_ten(numerator))
    additional_denominator = convert_additional(convert_ten(denominator))
    check_type_fraction = sum_additional(additional_numerator, additional_denominator)
    if check_type_fraction[0] == '0':
        while numerator[0] != '1':
            numerator = sum_additional(numerator, convert_additional(convert_ten(denominator)))
            if numerator[0] != '1':
                integer = sum_additional("".join(integer), "".join(ONE))
    if list(integer) == ZERO:
        return integer
    if flag:
        return '1' + integer[1:]
    else:
        return integer

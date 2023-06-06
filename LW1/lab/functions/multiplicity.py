from lab.functions.convert_to_bin import *
from lab.functions.sum import *
from lab.settings import *


def multiplicity(factor_1: str, factor_2: str) -> list[str]:
    result = ZERO
    flag = factor_1[0] == factor_2[0]
    if factor_2[0] == '1':
        factor_2 = '0' + factor_2[1:]
    while factor_2 != ''.join(ZERO):
        additional_factor_1 = convert_additional(convert_ten(factor_1))
        additional_result = convert_additional(convert_ten("".join(result)))
        result = sum_additional(additional_factor_1, additional_result)
        factor_2 = sum_additional(convert_additional(convert_ten(factor_2)), ''.join(ONE_ADDITION))
    if flag:
        result = '0' + result[1:]
    else:
        result = '1' + result[1:]
    return result

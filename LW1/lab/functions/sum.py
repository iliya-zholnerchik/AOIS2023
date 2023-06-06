from typing import List
from lab.settings import *


def sum_additional(f: str, s: str) -> str:
    term1, term2 = list(f), list(s)
    addition_result = spacing(term1, term2)
    if len(addition_result) > BIT:
        addition_result.pop(0)
    if addition_result[0] == "1":
        for i in range(1, len(addition_result)):
            if addition_result[i] == "0":
                addition_result[i] = "1"
            else:
                addition_result[i] = "0"
        for i in range(len(addition_result) - 1, -1, -1):
            if addition_result[i] == "0":
                addition_result[i] = "1"
                break
            if addition_result[i] == "1":
                addition_result[i] = "0"
    return "".join(addition_result)


def spacing(first_element: List[str], second_element: List[str]) -> List[str]:
    carry = 0
    result = []
    for f, s in zip(reversed(first_element), reversed(second_element)):
        s = int(f) + int(s) + carry
        result.append(str(s % 2))
        carry = s // 2
    if carry:
        result.append(str(carry))
    return result[::-1] if result else ["0"]

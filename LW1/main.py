from lab.functions.multiplicity import *
from lab.functions.divide import *
from lab.functions.sum_float_point import *


def main():

    f = int(input("Enter first number: "))
    s = int(input("Enter second number: "))

    print("\n\tTranslating:\n")

    print(f"X1 = {f}", convert_straight(f), convert_reverse(f), convert_additional(f), sep="\n")
    print(f"-X1 = {-f}", convert_straight(-f), convert_reverse(-f), convert_additional(-f), sep="\n")
    print(f"X2 = {s}", convert_straight(s), convert_reverse(s), convert_additional(s), sep="\n")
    print(f"X2 = {-s}", convert_straight(-s), convert_reverse(-s), convert_additional(-s), sep="\n")

    print("\n\tSum:\n")

    print(f"X1 + X2 = {f + s}")
    print(sum_additional(convert_additional(f), convert_additional(s)))
    print(f"X1 - X2 = {f - s}")
    print(sum_additional(convert_additional(f), convert_additional(-s)))
    print(f"-X1 + X2 = {-f + s}")
    print(sum_additional(convert_additional(-f), convert_additional(s)))
    print(f"-X1 - X2 = {-f - s}")
    print(sum_additional(convert_additional(-f), convert_additional(-s)))

    print("\n\tMultiplicity:\n")

    print(f"X1 * X2 = {f * s}")
    print(multiplicity(convert_straight(f), convert_straight(s)))
    print(f"X1 * (-X2) = {f * (-s)}")
    print(multiplicity(convert_straight(f), convert_straight(-s)))
    print(f"(-X1) * X2 = {(-f) * s}")
    print(multiplicity(convert_straight(-f), convert_straight(s)))
    print(f"(-X1) * (-X2) = {(-f) * (-s)}")
    print(multiplicity(convert_straight(-f), convert_straight(-s)))

    print("\n\tDivide:\n")

    print(f"X1 / X2 = {f / s}")
    print(divide(convert_straight(f), convert_straight(s)))
    print(f"X1 / (-X2) = {f / (-s)}")
    print(divide(convert_straight(f), convert_straight(-s)))
    print(f"(-X1) / X2 = {(-f) / s}")
    print(divide(convert_straight(-f), convert_straight(s)))
    print(f"(-X1) / (-X2) = {(-f) / (-s)}")
    print(divide(convert_straight(-f), convert_straight(-s)))

    print("\n\tSum in float:\n")

    float_a = input("Enter first number (in *.* format): ")
    float_b = input("Enter second number (in *.* format): ")

    print(sum_float(float_a, float_b))


if __name__ == "__main__":
    main()

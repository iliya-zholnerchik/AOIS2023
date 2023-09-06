from lab.functions.multiplicity import *
from lab.functions.divide import *
from lab.functions.sum_float_point import *

class BinaryOperations:
    class BinaryFloatRepresentation:
        sign = ''
        order = ''
        mantissa = ''

    imaginary_unit = 0

    def lead_string_to_some_digit_view(self, binary_representation, amount):
        while len(binary_representation) < int(amount):
            binary_representation = '0' + binary_representation
        return binary_representation

    def convert_int_to_binary_representation(self, int_number):
        greater_then_zero = int_number >= 0
        result = ''

        while abs(int(int_number)) >= 1:
            result = str(abs(int(int_number)) % 2) + str(result)
            int_number = int(int_number) / 2

        if not greater_then_zero:
            return '1' + self.lead_string_to_some_digit_view(result, 15)

        return self.lead_string_to_some_digit_view(result, 16)

    def convert_part_of_float_after_dot_to_binary_representation(self, part_after_dot):
        counter = -1
        result = ''
        while part_after_dot > 0:
            if part_after_dot - pow(2, counter) >= 0:
                result = result + '1'
                part_after_dot = round(part_after_dot - pow(2, counter), 5)
            else:
                result = result + '0'
            counter -= 1
        return result

    def convert_to_binary_float(self, float_number):
        binary_float = self.BinaryFloatRepresentation()

        binary_float.sign = '0' if float_number >= 0 else '1'

        part_of_float_before_dot = str(float_number).split('.')[0]
        part_of_float_after_dot = round(float_number - int(part_of_float_before_dot), 10)
        binary_part_of_float_before_dot = str(int(self.convert_int_to_binary_representation(
            int(part_of_float_before_dot))))
        binary_float.order = self.lead_string_to_some_digit_view(
            str(int(self.convert_int_to_binary_representation(len(binary_part_of_float_before_dot) + 126))), 8)
        result = binary_part_of_float_before_dot[1:] + self.convert_part_of_float_after_dot_to_binary_representation(
            part_of_float_after_dot)
        while len(result) != 23:
            result = result + '0'

        binary_float.mantissa = result
        return binary_float

    def mantissa_shift(self, binary_representation, shift):
        for i in range(0, shift):
            if i == 0:
                binary_representation = binary_representation[:1] + '1' + binary_representation[1:]
            else:
                binary_representation = binary_representation[:1] + '0' + binary_representation[1:]
        binary_representation = binary_representation[:len(binary_representation) - shift]
        return binary_representation

    def sum_of_float_representation(self, float_representation_1, float_representation_2):
        result = self.BinaryFloatRepresentation()
        result.sign = '0'

        mantissa_1 = '0' + float_representation_1.mantissa
        mantissa_2 = '0' + float_representation_2.mantissa

        if float_representation_1.order != float_representation_2.order:
            difference_of_order = self.convert_binary_representation_to_int('0' + float_representation_1.order)\
                                  - self.convert_binary_representation_to_int('0' + float_representation_2.order)
            if difference_of_order < 0:
                mantissa_1 = self.mantissa_shift(mantissa_1, abs(difference_of_order))
                result.order = float_representation_2.order
                print(str(float_representation_1.sign) + ' ' + str(float_representation_2.order) + ' '
                      + str(mantissa_1[1:]))
            if difference_of_order > 0:
                mantissa_2 = self.mantissa_shift(mantissa_2, abs(difference_of_order))
                result.order = float_representation_1.order
                print(str(float_representation_1.sign) + ' ' + str(float_representation_1.order) + ' '
                      + str(mantissa_2[1:]))
        else:
            result.order = float_representation_1.order
        sum_of_mantissa = ''
        for i in range(len(mantissa_1) - 1, 0, -1):
            sum_of_mantissa = str(self.summing_bytes(mantissa_1[i], mantissa_2[i])) + str(sum_of_mantissa)
        self.imaginary_unit = 0
        if sum_of_mantissa[0] == '1':
            result.order = self.lead_string_to_some_digit_view(str(int(self.sum_of_binary_representation(
                result.order, '1'))), 8)
            sum_of_mantissa = sum_of_mantissa[1:]
        result.mantissa = sum_of_mantissa
        return result

    def convert_binary_representation_to_int(self, binary_representation):
        result = 0
        for i in range(1, len(binary_representation)):
            result += pow(2, len(binary_representation) - 1 - i) * int(binary_representation[i])
        if binary_representation[0] == '0':
            return result
        return -1 * result

    def summing_bytes(self, byte_1, byte_2):
        amount_of_bytes = int(byte_1) + int(byte_2) + self.imaginary_unit
        if amount_of_bytes < 2:
            output = str(amount_of_bytes)
            self.imaginary_unit = 0
        else:
            output = str(amount_of_bytes - 2)
            self.imaginary_unit = 1
        return output

    def sum_of_binary_representation(self, binary_representation_1, binary_representation_2):
        result = ''
        binary_representation_1 = self.lead_string_to_some_digit_view(binary_representation_1, 16)
        binary_representation_2 = self.lead_string_to_some_digit_view(binary_representation_2, 16)
        for i in range(15, 0, -1):
            result = str(self.summing_bytes(binary_representation_1[i], binary_representation_2[i])) + str(result)
        self.imaginary_unit = 0
        return result

    def convert_binary_representation_to_float(self, binary_representation):
        order = self.convert_binary_representation_to_int('0' + binary_representation.order) - 127
        buffer = 0
        for i in range(0, len(binary_representation.mantissa)):
            buffer = buffer + int(str(binary_representation.mantissa[i])) * float(pow(2, -(i+1)))
        return (1 + buffer) * pow(2, order)

    def summing_float(self, number_1, number_2):
        float_binary_representation_1 = binary.convert_to_binary_float(float(number_1))
        print(str(float_binary_representation_1.sign) + ' ' + str(float_binary_representation_1.order) + ' ' + str(
            float_binary_representation_1.mantissa))
        float_binary_representation_2 = binary.convert_to_binary_float(float(number_2))
        print(str(float_binary_representation_2.sign) + ' ' + str(float_binary_representation_2.order) + ' ' + str(
            float_binary_representation_2.mantissa))
        result_binary_representation = binary.sum_of_float_representation(binary.convert_to_binary_float(float(
            number_1)), binary.convert_to_binary_float(float(number_2)))
        print(str(result_binary_representation.sign) + ' ' + str(result_binary_representation.order) + ' ' + str(
            result_binary_representation.mantissa))
        print(self.convert_binary_representation_to_float(result_binary_representation))


    def reversing_binary_representation(self, binary_representation):
        sign = binary_representation[0]
        binary_representation = self.lead_string_to_some_digit_view(binary_representation[1:], 15)
        result = ''
        for i in range(0, 15):
            if binary_representation[i] == '1':
                result = result + '0'
            else:
                result = result + '1'
        return sign + result

    def convert_binary_direct_representation_to_additional(self, binary_direct_representation):
        if binary_direct_representation[0] == '0':
            return binary_direct_representation
        else:
            return self.sum_of_binary_representation(self.reversing_binary_representation(
                binary_direct_representation), '01')

    def convert_binary_additional_representation_to_direct(self, additional_representation):
        if additional_representation[0] == '1':
            additional_representation = '1' + self.sum_of_binary_representation(self.reversing_binary_representation(
                additional_representation), '1')[1:]
            return self.convert_binary_representation_to_int(additional_representation)

    def sum_of_terms(self, term):
        result = ''
        for t in term:
            result = self.sum_of_binary_representation(result, t)
        return result

    def multiplication_int(self, int_number_1, int_number_2):
        binary_representation_1 = self.convert_int_to_binary_representation(int_number_1)
        binary_representation_2 = self.convert_int_to_binary_representation(int_number_2)
        term = []
        if binary_representation_1[0] == binary_representation_2[0]:
            result = '0'
        else:
            result = '1'
        binary_representation_2 = binary_representation_2[1:]
        for i in range(0, len(binary_representation_2)):
            term.append(self.lead_string_to_some_digit_view(str(int(binary_representation_1[1:]) * int(
                binary_representation_2[len(binary_representation_2) - 1 - i]) * pow(10, i)), 16))
        result = result + str(self.sum_of_terms(term)[1:])
        print(binary_representation_1 + '\n+\n' + binary_representation_2)
        print(result)
        print(self.convert_binary_representation_to_int(result))
        return result

    def minus_bytes(self, byte_1, byte_2):
        minus_of_bytes = int(byte_1) - int(byte_2) - int(self.imaginary_unit)
        if minus_of_bytes >= 0:
            output = str(minus_of_bytes)
            self.imaginary_unit = 0
        else:
            self.imaginary_unit = 1
            output = str(minus_of_bytes + 2)
        return output

    def minus_binary_representation(self, binary_representation_1, binary_representation_2):
        output = ''
        binary_representation_1 = self.lead_string_to_some_digit_view(binary_representation_1, 16)
        binary_representation_2 = self.lead_string_to_some_digit_view(binary_representation_2, 16)
        for index in range(15, 0, -1):
            output = str(self.minus_bytes(binary_representation_1[index], binary_representation_2[index])) + str(output)
        self.imaginary_unit = 0
        return output

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



if __name__ == "__main__":
    main()
    binary = BinaryOperations()
    binary.summing_float(0.5, 0.125)

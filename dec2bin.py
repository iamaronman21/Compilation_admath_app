def dec2bin(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_number = ""
    is_negative = False

    if decimal_num < 0:
        is_negative = True
        decimal_num = abs(decimal_num)

    while decimal_num > 0:
        binary_number = str(decimal_num % 2) + binary_number
        decimal_num //= 2

    if is_negative:
        binary_number = '-' + binary_number

    return binary_number

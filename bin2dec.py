def bin2dec(binary_num):

    is_negative = False
    if binary_num[0] == '-':
        is_negative = True
        binary_num = binary_num[1:]

    decimal_num = 0
    power = len(binary_num) - 1

    for digit in binary_num:
        if digit == '1':
            decimal_num += 2 ** power
        power -= 1

    if is_negative:
        decimal_num *= -1

    return decimal_num


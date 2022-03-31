def print_formatted(number):
    for i in range(number):
        i += 1
        print(i, str(oct(i)[2:]), str(hex(i)[2:]), str(bin(i)[2:]))

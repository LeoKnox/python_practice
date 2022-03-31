def print_formatted(number):
    width = len(str(bin(number)[2:]))
    print(width)
    for i in range(number):
        i += 1
        print(i, str(oct(i)[2:]), str(hex(i)[2:]), str(bin(i)[2:]))

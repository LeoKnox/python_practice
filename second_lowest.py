if __name__ == '__main__':
    low = 10000
    second = 10000
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        print(low, second)
        print(grades)
        if score < low:
            second = low
            low = score
        elif score < second:
            second = score
        if score in grades:
            grades[score].append(name)
        else:
            grades[score] = [name]
    grades[second].sort()
    for g in grades[second]:
        print(g)

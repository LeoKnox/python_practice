if __name__ == '__main__':
    low = []
    ans = []
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in grades:
            grades[score].append(name)
        else:
            grades[score] = [name]
        print(name, str(score))
        low.append((name, score))
    print(grades)

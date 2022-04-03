if __name__ == '__main__':
    low = []
    ans = []
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in grades:
            print("dupe")
            grades[score].append(name)
        else:
            grades[score] = [name]
        print(name, str(score))
        grades[score] = name
        low.append((name, score))
    print(grades)

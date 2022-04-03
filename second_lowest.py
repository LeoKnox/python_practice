    low = []
    ans = []
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if grades[score]:
            print("dupe")
        else:
            grades[score]= name
        print(name, score)
        low.append((name, score))
    print(low)
    print(grades)

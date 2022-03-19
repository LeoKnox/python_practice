    lowest = 0
    second = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        print(name + " " + str(score))
        if lowest == 0:
            lowest = score
        elif score < lowest:
            second = lowest
            lowest = score
    print (lowest)
    print (second)

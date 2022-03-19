    for _ in range(int(input())):
        name = input()
        score = float(input())
        lowest = {}
        second = []
        print(name + " " + str(score))
        if lowest:
            second = lowest
            lowest = score
        else:
            lowest = {name: score}
            
    print (lowest)
    print (lowest.score)

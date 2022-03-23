    lowest = []
    second = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = (name, score)
        print(name + " " + str(score))
        # check if lowest variable exists
        if len(lowest) > 0:
            #compare if score is lower assign lowest to second lowest
            if (lowest[1] > student[1]):
                print("*")
                second[0] = (lowest[0], lowest[1])
                lowest[0] = name
                lowest[1] = score
                print(lowest)
                print(second)
            #compare if score equals lowest add sorted to array
            #compare if score is lower then second score to second
            elif (second[0][1] > score):
                print("**")
                print(second)
                second = (name, score)
        # if lowest is empty assign first score
        else:
            print("!")
            lowest.append(name)
            lowest.append(score)
            second = [lowest]
    print (lowest)
    print (second)

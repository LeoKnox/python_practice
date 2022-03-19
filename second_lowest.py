for _ in range(int(input())):
        name = input()
        score = float(input())
        lowest = []
        second = []
        print(name + " " + str(score))
        # check if lowest variable exists
        if lowest:
            pass
            #compare if score is lower assign lowest to second lowest
            if lowest[0] > score:
                second = [lowest]
                lowest[0] = name
                lowest[1] = score
            #compare if score is lower then second score to second
            #compare if score equals lowest add sorted to array
        # if lowest is empty assign first score
        else:
            lowest.append(name)
            lowest.append(score)
            
    print (second)

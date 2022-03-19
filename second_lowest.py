    for _ in range(int(input())):
        name = input()
        score = float(input())
        lowest = {}
        second = []
        print(name + " " + str(score))
        # check if lowest variable exists
        if lowest:
            second = lowest
            lowest = score
            #compare if score is lower assign lowest to second lowest
            #compare if score is lower then second score to second
            #compare if score equals lowest add sorted to array
        # if lowest is empty assign first score
        else:
            lowest = {name: score}
            
    print (lowest)
    print (lowest.score)

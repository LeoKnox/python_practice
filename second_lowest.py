if __name__ == '__main__':
    lowest = []
    second = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        print(name + " " + str(score))
        # check if lowest variable exists
        if len(lowest) > 0:
            #compare if score is lower assign lowest to second lowest
            if (lowest[1] > score):
                print("*")
                print(lowest)
                second[0] = lowest
                lowest[0] = name
                lowest[1] = score
                print(second)
            #compare if score equals lowest add sorted to array
            #compare if score is lower then second score to second
            elif (second[0][1] > score):
                print(second)
        # if lowest is empty assign first score
        else:
            lowest.append(name)
            lowest.append(score)
            second = [lowest]
    print (lowest)
    print (second)

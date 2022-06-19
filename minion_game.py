def minion_game(string):
    minions = {}
    vowels = {'A', 'E', 'I', 'O', 'U'}
    i = 0
    while i < len(string):
        if string[i] not in vowels:
            for j in range(len(string)):
                minions[string[j:i]] = minions.get(string[j:i], 0) + 1
            #minions[string[i]] = minions.get(string[i], 0) + 1
        i += 1
        for j in range(len(string)):
            print(string[j:i])
    print(minions)

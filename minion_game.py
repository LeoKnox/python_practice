def minion_game(string):
    minions = {}
    vowels = {'A', 'E', 'I', 'O', 'U'}
    i = 0
    while i < len(string):
        if string[i] not in vowels:
            minions[string[i]] = minions.get(string[i], 0) + 1
        i += 1
    print(minions)
    for j in range(len(string)):
        print(j)

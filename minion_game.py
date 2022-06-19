def minion_game(string):
    minions = {}
    vowels = {'A', 'E', 'I', 'O', 'U'}
    i = 0
    total = 0
    while i < len(string):
        i += 1
        for j in range(len(string)):
            minions[string[j:i]] = minions.get(string[j:i], 0) + 1
        for j in range(len(string)):
            print(string[j:i])
    print(minions)
    minions[''] = 0
    for m in minions:
        if m not in vowels or m != '':
            total += minions[m]
    print(total)

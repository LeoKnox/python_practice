def minion_game(string):
    minions = {}
    vowels = {'A', 'E', 'I', 'O', 'U'}
    i = 0
    stuart = 0
    kevin = 0
    while i < len(string):
        i += 1
        for j in range(len(string)):
            minions[string[j:i]] = minions.get(string[j:i], 0) + 1
        #for j in range(len(string)):
            #print(string[j:i])
    del minions['']
    #print(minions)
    for m in minions:
        if ((m not in vowels) and not (m.startswith("A"))):
            stuart += minions[m]
        if ((m in vowels) and (m.startswith("A"))):
            kevin += minions[m]
    #print(stuart, " ", kevin)
    if stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Kevin", kevin)

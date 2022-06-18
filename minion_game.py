def minion_game(string):
    minions = {}
    vowels = {'A', 'e', 'i', 'o', 'u'}
    i = 0
    while i < len(string):
        if string[i] not in vowels:
            print(string[i])
        i += 1

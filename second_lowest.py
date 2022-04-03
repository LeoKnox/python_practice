if __name__ == '__main__':
    low = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if len(low) > 0:
            print("dupe")
        else:
            low.append((name, score))
        print(name, score)
        low.append((name, score))
    print(low)

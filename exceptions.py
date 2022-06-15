for j in range(int(input())):
    x = (input().split())
    try:
        print(int(x[0])//int(x[1]))
    except Exception as e:
        print("Error Code:",e)

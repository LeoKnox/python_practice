i = int(input())
newarr = []
for j in range(i):
    x = (input().split())
    try:
        print(int(x[0])//int(x[1]))
    except Exception as e:
        print("Error Code:",e)

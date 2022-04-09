from collections import Counter

cnt = input()
new_arr = Counter(input())
sum = 0
print(new_arr)
cnt = input()

for i in range(0, int(cnt)):
    ans = input().split(" ")
    print(ans)
    if ans:
        sum += 1
    new_arr[i] -= 1
print (sum)

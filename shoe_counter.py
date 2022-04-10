from collections import Counter

cnt = input()
new_arr = Counter(input())
sum = 0
print(new_arr)
cnt = input()

for i in range(0, int(cnt)):
    ans = input().split(" ")
    print(ans)
    if new_arr[ans[0]] and new_arr[ans[0]]> 0:
        sum += int(ans[1])
    new_arr[ans[0]] -= 1
print (sum)

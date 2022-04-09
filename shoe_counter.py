from collections import Counter

cnt = input()
new_arr = Counter(input())
sum = 0
print(new_arr)

for i in range(0, int(cnt)-3):
    ans = input()
    print(ans)
    sum += new_arr[i]
    new_arr[i] -= 1
print (sum)

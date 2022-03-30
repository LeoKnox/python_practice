if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    ans = []
    exit = 0
    for _ in range(n):
        total = 0
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        for x in scores:
            total += x
        total = total/len(scores)
        ans.append({name, total})
        print(name)
        print(total)
    print (ans)
    query_name = input()

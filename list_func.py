if __name__ == '__main__':
    N = int(input())
    ans = []
    comm = ""
    for i in range(N):
        command = input()
        command = command.split(" ")
        comm = ",".join([i for i in command[1:]])
        if command[0] != "print":
            eval("ans." + command[0] + "(" + comm + ")")
        else:
            print(ans)

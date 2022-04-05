if __name__ == '__main__':
    N = int(input())
    ans = []
    #print(N)
    comm = ""
    for i in range(N):
        command = input()
        command = command.split(" ")
        #ans[command](*args)
        comm = ",".join([i for i in command[1:]])
        #print(eval(command[0], *command[1:]), comm)
        print(comm)

'''
n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tuple_list = ()
    tuple_list(tuple(integer_list))
    print('N:', n)
    print('il:', integer_list)
    print('h:', hash(tuple_list))
'''
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))

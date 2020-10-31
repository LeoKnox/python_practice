def identity(f):
    return f

@identity
def foo():
    return 'bar'

foo = identity(foo)
print(foo)
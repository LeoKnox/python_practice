_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register
def foo():
    return 'bar'

foo = register(foo)
print (foo)

'''
def identity(f):
    return f

@identity
def foo():
    return 'bar'

foo = identity('foo')
print(foo)
'''
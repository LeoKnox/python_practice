class one(object):
    one = 'this is one from one'


class two(object):
    one = 'this is one of two'
    two = 'this is two of two'

class borg(two, one):
    borg = 'Assimilate'

b = borg()
print (b.one)

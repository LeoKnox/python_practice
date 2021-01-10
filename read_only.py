class Character(object):
    def __init__(name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max = max_hp
        
    @property
    def hp(self):
        return self._hp

class Character(object):
    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max = max_hp
        
    @property
    def hp(self):
        return self._hp
    
    @property
    def name(self):
        return self.name
    
    def take_damage(self, damage):
        self.hp -= damage
        self.hp = 0 if self.hp <0 else self.hp
    
    @property
    def is_alive(self):
        return self.hp !=0
    
    @property
    def is_wounded(self):
        return self.hp < self.max_hp if self.hp > 0 else False
    
    @property
    def Is_dead(self):
        return not self.is_alive

elric = Character('Elric', 100)
print(elric.hp)

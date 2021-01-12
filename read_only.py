class Character(object):
    def __init__(self, name, max_hp, damage_bonus=3):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp
        self._damage_bonus = damage_bonus
        
    @property
    def hp(self):
        return self._hp
    
    @property
    def name(self):
        return self.name
    
    def take_damage(self, damage):
        self._hp -= damage + self._damage_bonus
        self._hp = 0 if self.hp <0 else self.hp
    
    @property
    def is_alive(self):
        return self.hp !=0
    
    @property
    def is_wounded(self):
        return self.hp < self._max_hp if self.hp > 0 else False
    
    @property
    def is_dead(self):
        return not self.is_alive

elric = Character('Elric', 100)
print(elric.hp)

print(elric.is_dead)
print(elric.is_wounded)
elric.take_damage(10)

print(elric.hp)
print(elric.is_wounded)

#elric.take_damage(1000)
print(elric.is_dead)

elric._damage_bonus = 11
elric.take_damage(10)
print(elric.hp)

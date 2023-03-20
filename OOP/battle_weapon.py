class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        return self.health > 0
    def hit(self, other):            # wchodzi jednostka zaatakowana
        other.loss(self.attack)        # odpal fukcje obrazen dla jednostki zaatakowanej i przekaz siłę jednostki atakujacej
    def damage(self, attack):           # sila jednostki atakujacej
        return attack
    def loss(self, attack):            # obnizenie zycia dla jednostki zaatakowanej z siłą jednostki atakujacej
        self.health -= self.damage(attack)
        
    def equip_weapon(self, weapon):
        for atr in filter(lambda a: not a.startswith('__'), vars(self)):
            setattr(self, atr, getattr(self, atr)+getattr(weapon, atr))
            if getattr(self, atr) < 0 : setattr(self, atr, 0)
            
class Warlord(Warrior):
    def __init__(self):
        super().__init__(health=100, attack=4)
        self.defense = 2
    def damage(self, attack):
        return max(0, attack - self.defense)   
        
class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)
        
class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2
    def damage(self, attack):
        return max(0, attack - self.defense)
    
class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50
    def hit(self, other):            # nadpisz metode
        super().hit(other)           # pobierz metody od rodzica
        self.health += other.damage(self.attack) * self.vampirism // 100        # dodaj jeszcze to
        
class Lancer(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=6)
    def hit(self, other, *args):
        other.loss(self.attack)
        if args : args[0].loss(self.attack/2)
        
class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.heal_power = 0
        
    def hit(self, other, *args):
        other.loss(self.attack)
        
    def heal(self, friend):
        friend.health += 2 + self.heal_power
        
class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power
        
    
class Sword(Weapon):
    def __init__(self):
        super().__init__(5, 2, 0, 0, 0)
class Shield(Weapon):
    def __init__(self):
        super().__init__(20, -1, 2, 0, 0)
        
class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(-15, 5, -2, 10, 0)
        
class Katana(Weapon):
    def __init__(self):
        super().__init__(-20, 6, -5, 50, 0)
        
class MagicWand(Weapon):
    def __init__(self):
        super().__init__(30, 3, 0, 0, 3)
        
        
def fight(unit_1, unit_2, *args):                        # tylko po to bo funkcja jest testowana przez dwa unity
    while 1:
        try:
            unit_1.hit(unit_2, args[1])
            if  isinstance(args[0], Healer): args[0].heal(unit_1)
        except:
            unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        try:
            unit_2.hit(unit_1, args[0])
            if  isinstance(args[1], Healer): args[1].heal(unit_2)
        except:
            unit_2.hit(unit_1)
        if unit_1.health <= 0:
            return False
        
class Army:
    def __init__(self):
        self.units = []
        
    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())
            
    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit
            
    @property
    def second_alive_unit(self):
        for ind, unit in enumerate(self.units):
            if unit.is_alive :
                try:
                    return self.units[ind +1]
                except:
                    return None
            
    @property
    def is_alive(self):
        return self.first_alive_unit is not None
    
    def move_units(self):
        print(self.units)
        for ind, unit in enumerate(self.units):
            if isinstance(unit, Lancer):
                print("kurwa")
                print(self.units.pop(ind), "\n")
                self.units.append(self.units.pop(ind))
                break
        print(self.units, "\n")
    
class Battle:                                       # battle.fight(my_army, enemy_army)
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.first_alive_unit, army_2.first_alive_unit, army_1.second_alive_unit, army_2.second_alive_unit)            # tutaj dodac dodatkwe arugmenty
        return army_1.is_alive
    
    @staticmethod
    def straight_fight(army_1, army_2):
        try:
            army_1 = army_1.units
            army_2 = army_2.units
        except:
            pass
        
        if not army_1: return False
        if not army_2: return True
        arm1, arm2 = [], []
        for unit1, unit2 in zip(army_1, army_2):
            if fight(unit1, unit2):
                arm1.append(unit1)
            else:
                arm2.append(unit2)
                
        if len(army_1) - len(army_2) < 0:
            arm2 += army_2[len(army_1):]
        elif len(army_1) - len(army_2) > 0:
            arm1 += army_1[len(army_2):]
                
                
        return Battle.straight_fight(arm1, arm2)
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ronald = Warlord()
	heimdall = Knight()

	assert fight(heimdall, ronald) == False

	my_army = Army()
	my_army.add_units(Warlord, 1)
	my_army.add_units(Warrior, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 2)

	enemy_army = Army()
	enemy_army.add_units(Warlord, 3)
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 2)
	enemy_army.add_units(Knight, 2)

	my_army.move_units()
	enemy_army.move_units()

	assert type(my_army.units[0]) == Lancer
	assert type(my_army.units[1]) == Healer
	assert type(my_army.units[-1]) == Warlord

	assert type(enemy_army.units[0]) == Vampire
	assert type(enemy_army.units[-1]) == Warlord
	assert type(enemy_army.units[-2]) == Knight

	#6, not 8, because only 1 Warlord per army could be
	assert len(enemy_army.units) == 6

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        return self.health > 0
    def hit(self, other, *args):            # wchodzi jednostka zaatakowana
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
    
class Rookie(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=1)
        self.health = 50
        self.attack = 1

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
    def hit(self, other, *args):            # nadpisz metode
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
        except Exception as e: 
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
        for ind, unit in reversed(list(enumerate(self.units))):         #clear dead units
            if not unit.is_alive: self.units.pop(ind)
        warlord = False
        army_list = []

        for ind, unit in (enumerate(self.units)):         # moving warlord to new list
            if isinstance(unit, Warlord):
                army_list.insert(-1, self.units.pop(ind))
                warlord = True
                break

        for ind, unit in reversed(list((enumerate(self.units)))):         # deleting others warlords
            if isinstance(unit, Warlord):
                self.units.pop(ind)

        if warlord:
            for class_name in [Lancer, Vampire, Warrior, Defender, Knight]:
                for ind, unit in reversed(list(enumerate(self.units))):        # moving lancer to front position
                    if isinstance(unit, class_name):
                        army_list.insert(0, self.units.pop(ind))
                        break
                else:
                    continue
                break

            for ind, unit in reversed(list(enumerate(self.units))):         # moving healers to second and further positions
                if isinstance(unit, Healer):
                    army_list.insert(1, self.units.pop(ind))

            for class_name in [Lancer, Defender, Knight]:
                for ind, unit in reversed(list(enumerate(self.units))):
                    if isinstance(unit, class_name):
                        army_list.insert(-1, self.units.pop(ind))

        army_list[-1:-1] = self.units
        self.units = army_list        
    
class Battle:                                       # battle.fight(my_army, enemy_army)
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            if fight(army_1.first_alive_unit, army_2.first_alive_unit, army_1.second_alive_unit, army_2.second_alive_unit):
                army_2.move_units()  
            else:
                army_1.move_units()           # tutaj dodac dodatkwe arugmenty
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
        arm1= Army()
        arm2= Army()
        for unit1, unit2 in zip(army_1, army_2):
            if fight(unit1, unit2):
                arm1.units.append(unit1)
            else:
                arm2.units.append(unit2)
                
        if len(army_1) - len(army_2) < 0:
            arm2.units += army_2[len(army_1):]
        elif len(army_1) - len(army_2) > 0:
            arm1.units += army_1[len(army_2):]
        arm1.move_units() 
        arm2.move_units() 
        
                
                
        return Battle.straight_fight(arm1, arm2)
    


army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 1)

army_2.add_units(Warlord, 5)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())


army_1.move_units()
army_2.move_units()
battle = Battle()
battle.straight_fight(army_1, army_2)


army_1 = Army()
army_2 = Army()
army_1.add_units(Warlord, 1)
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 2)
army_1.add_units(Healer, 2)
army_2.add_units(Warlord, 1)
army_2.add_units(Vampire, 1)
army_2.add_units(Healer, 2)
army_2.add_units(Knight, 2)
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.fight(army_1, army_2)
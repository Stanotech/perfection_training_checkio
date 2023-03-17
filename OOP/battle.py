class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):            # wchodzi jednostka zaatakowana
        # odpal fukcje obrazen dla jednostki zaatakowanej i przekaz siłę jednostki atakujacej
        other.loss(self.attack)

    def damage(self, attack):           # sila jednostki atakujacej
        return attack

    # obnizenie zycia dla jednostki zaatakowanej z siłą jednostki atakujacej
    def loss(self, attack):
        self.health -= self.damage(attack)


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
        # dodaj jeszcze to
        self.health += other.damage(self.attack) * self.vampirism // 100


class Lancer(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=6)

    def hit(self, other, *args):
        other.loss(self.attack)
        if args: args[0].loss(self.attack/2)


class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)

    def hit(self, other, *args):
        other.loss(self.attack)

    def heal(self, friend):
        friend.health += 2


# tylko po to bo funkcja jest testowana przez dwa unity
def fight(unit_1, unit_2, *args):
    while 1:
        try:
            unit_1.hit(unit_2, args[1])
            if isinstance(args[0], Healer): args[0].heal(unit_1)
        except:
            unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        try:
            unit_2.hit(unit_1, args[0])
            if isinstance(args[1], Healer): args[1].heal(unit_2)
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
            if unit.is_alive:
                try:
                    return self.units[ind + 1]
                except:
                    return None

    @property
    def is_alive(self):
        return self.first_alive_unit is not None


# battle.fight(my_army, enemy_army)
class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.first_alive_unit, army_2.first_alive_unit, army_1.second_alive_unit,
                  army_2.second_alive_unit)            # tutaj dodac dodatkwe arugmenty
        return army_1.is_alive

    @staticmethod
    def straight_fight(army_1, army_2):
        print("jop")
        try:
            army_1 = army_1.units
            army_2 = army_2.units
        except:
            pass

        print(army_1, "\n")
        print(army_2)
        if not army_1: return False
        if not army_2: return True
        arm1, arm2 = [], []

        for unit1, unit2 in zip(army_1, army_2):
            if fight(unit1, unit2):
                print(unit1.health)
                print(unit2.health, "\n")
                arm1.append(unit1)
            else:
                print(unit2)
                print(unit1.health)
                print(unit2.health, "\n")
                arm2.append(unit2)

        if len(army_1) - len(army_2) < 0:
            arm2 += army_2[len(army_1):]
        elif len(army_1) - len(army_2) > 0:
            arm1 += army_1[len(army_2):]

        return Battle.straight_fight(arm1, arm2)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)
    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)
    battle = Battle()
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16
    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)
    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)
    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)
    battle = Battle()
    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing



    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)



    battle = Battle()


    assert battle.straight_fight(army_3, army_4) == False

    # army_1 = Army()
    # army_2 = Army()
    # army_1.add_units(Lancer, 4)
    # army_1.add_units(Warrior, 3)
    # army_1.add_units(Healer, 1)
    # army_1.add_units(Warrior, 4)
    # army_1.add_units(Healer, 1)
    # army_1.add_units(Knight, 2)
    # army_2.add_units(Warrior, 4)
    # army_2.add_units(Defender, 4)
    # army_2.add_units(Healer, 1)
    # army_2.add_units(Vampire, 2)
    # army_2.add_units(Lancer, 4)
    # battle = Battle()
    # battle.straight_fight(army_1, army_2)
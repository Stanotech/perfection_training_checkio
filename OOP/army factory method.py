class Army:
    def train_swordsman(self, name): return Swordsman(name, self.__class__.__name__ )    
    def train_lancer(self, name): return Lancer(name, self.__class__.__name__ )    
    def train_archer(self, name): return Archer(name, self.__class__.__name__ )

class Unit:
    def __init__(self, name, army_type):
        self.name = name
        self.army_type = army_type

    def introduce(self):
        return (f"{self.unit_type} {self.name}, {self.army_type[:-4]} {self.__class__.__name__.lower() }")

class Swordsman(Unit):
    def __init__(self, name, army_type):
        super().__init__(name, army_type)
        self.unit_type = "Knight" if army_type == "EuropeanArmy" else "Samurai"    

class Lancer(Unit):
    def __init__(self, name, army_type):
        super().__init__(name, army_type)
        self.unit_type = "Raubritter" if army_type == "EuropeanArmy" else "Ronin"

class Archer(Unit):
    def __init__(self, name, army_type):
        super().__init__(name, army_type)
        self.unit_type = "Ranger" if army_type == "EuropeanArmy" else "Shinobi"

class AsianArmy(Army): pass
class EuropeanArmy(Army): pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"
    
    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"


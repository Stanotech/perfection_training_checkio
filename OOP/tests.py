

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
battle.fight(army_1, army_2)

zeus = Knight()
godkiller = Warrior()
fight(zeus, godkiller)
zeus.is_alive


unit_1 = Defender()
unit_2 = Vampire()
weapon_1 = Shield()
weapon_2 = MagicWand()
weapon_3 = Shield()
weapon_4 = Katana()
unit_1.equip_weapon(weapon_1)
unit_1.equip_weapon(weapon_2)
unit_2.equip_weapon(weapon_3)
unit_2.equip_weapon(weapon_4)
fight(unit_1, unit_2)

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_2.add_units(Warrior, 11)
battle = Battle()
battle.fight(army_1, army_2)

husband = Warrior()
wife = Warrior()
fight(husband, wife)
wife.is_alive

weapon_1 = MagicWand()
weapon_2 = GreatAxe()
my_army = Army()
my_army.add_units(Knight, 1)
my_army.add_units(Lancer, 1)
enemy_army = Army()
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 1)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
battle = Battle()
battle.fight(my_army, enemy_army)

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 11)
army_2.add_units(Warrior, 7)
battle = Battle()
battle.fight(army_1, army_2)

dragon = Warrior()
knight = Knight()
fight(dragon, knight)
knight.is_alive

weapon_1 = Sword()
weapon_2 = GreatAxe()
my_army = Army()
my_army.add_units(Defender, 1)
my_army.add_units(Warrior, 1)
enemy_army = Army()
enemy_army.add_units(Knight, 1)
enemy_army.add_units(Healer, 1)
my_army.units[0].equip_weapon(weapon_2)
my_army.units[1].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_1)
battle = Battle()
battle.fight(my_army, enemy_army)

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 5)
army_1.add_units(Defender, 4)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 4)
battle = Battle()
battle.fight(army_1, army_2)

unit_1 = Warrior()
unit_2 = Knight()
unit_3 = Warrior()
fight(unit_1, unit_2)
fight(unit_2, unit_3)

weapon_1 = Katana()
weapon_2 = Shield()
my_army = Army()
my_army.add_units(Defender, 2)
enemy_army = Army()
enemy_army.add_units(Knight, 1)
enemy_army.add_units(Vampire, 1)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapo

army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 5)
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
army_1.add_units(Defender, 4)
battle = Battle()
battle.fight(army_1, army_2)

unit_1 = Defender()
unit_2 = Rookie()
fight(unit_1, unit_2)
unit_1.health

weapon_1 = Weapon(-20, 6, 1, 40, -2)
weapon_2 = Weapon(20, -2, 2, -55, 3)
my_army = Army()
my_army.add_units(Knight, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
battle.fight(my_army, enemy_army)

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 5)
army_1.add_units(Defender, 10)
battle = Battle()
battle.fight(army_1, army_2)

unit_1 = Defender()
unit_2 = Rookie()
unit_3 = Warrior()
fight(unit_1, unit_2)
fight(unit_1, unit_3)



weapon_1 = Weapon(-20, 1, 1, 40, -2)
weapon_2 = Weapon(20, 2, 2, -55, 3)
my_army = Army()
my_army.add_units(Vampire, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
battle.straight_fight(my_army, enemy_army)
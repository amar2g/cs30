class Type:
    def __init__(self, name, weak, resist, immune):
        self.name = name
        self.weak = weak
        self.resist = resist
        self.immune = immune

    def get_name(self): 
        return self.name

    def is_weak_against(self, other):
        return other.get_name() in self.weak

    def is_resistant_to(self, other): 
        return other.get_name() in self.resist

    def is_immune_to(self, other): 
        return other.get_name() in self.immune

class Attack:
    def __init__(self, name, damage, attacktype):
        self.name = name
        self.damage = damage
        self.type = attacktype

    def get_damage(self):
        return self.damage

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name


class Pokemon:
    def __init__(self, name, poketype, attacks): # pokemon: name, type, 100 hp, 2 attacks
        self.name = name
        self.type = poketype
        self.hp = 100
        self.attacks = attacks
        self.fainted = False

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_type(self):
        return self.type

    def get_attacks(self):
        return self.attacks

    def is_fainted(self): 
        return self.fainted

    def take_damage(self, damage): # appyl damage and check for fainting
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.fainted = True

class Trainer:
    def __init__(self, name, pokemon): # trainer: nasme and pokemon list
        self.name = name
        self.pokemon = pokemon

    def get_name(self):
        return self.name

    def get_pokemon(self):
        return self.pokemon

    def can_battle(self): # check if trainer still has usable pokemon
        for p in self.pokemon:
            if not p.is_fainted():
                return True
        return False

    def choose_pokemon(self): # give trainer opt/ to choose a unfainted pokemon
        while True:
            print(f"\n{self.name} choose a pokemon: ")
            for i, p in enumerate(self.pokemon):
                status = "**fainted**" if p.is_fainted() else f"{p.get_hp()} hp"
                print(f"{i + 1}. {p.get_name()} ({status})")

            choice = input("enter num: ")

            # data validation
            if not choice.isdigit(): 
                print("error, invalid input")
                continue

            choice = int(choice) - 1

            if choice < 0 or choice >= len(self.pokemon):
                print("error, num out of range")
                continue

            if self.pokemon[choice].is_fainted():
                print("pokemon has fainted")
                continue

            return self.pokemon[choice]

class Battle:
    def __init__(self, trainer1, trainer2):
        self.t1 = trainer1
        self.t2 = trainer2

    def calc_damage(self, attacker, defender, attack):
        damage = attack.get_damage()
        atktype = attack.get_type()
        deftype = defender.get_type()

        # damage accvording to type
        if deftype.is_immune_to(atktype):
            return 0
        if deftype.is_weak_against(atktype):
            return damage * 2
        if deftype.is_resistant_to(atktype):
            return damage // 2

        return damage

    def choose_attack(self, pokemon, trainername):
        while True:
            print(f"\n{trainername} choose a attack")
            for i, a in enumerate(pokemon.get_attacks()):
                print(f"{i + 1}. {a.get_name()}")

            choice = input("enter num: ")
            
            # data validation
            if not choice.isdigit():
                print("error, invalid input")
                continue

            choice = int(choice) - 1

            if choice < 0 or choice >= len(pokemon.get_attacks()):
                print("erorr, num out of range")
                continue

            return pokemon.get_attacks()[choice]

    def start(self):
        p1 = self.t1.choose_pokemon()
        p2 = self.t2.choose_pokemon()

        while self.t1.can_battle() and self.t2.can_battle():
            print(f"\n{p1.get_name()} hp: {p1.get_hp()} --- {p2.get_name()} hp: {p2.get_hp()}")

            a1 = self.choose_attack(p1, self.t1.get_name())
            a2 = self.choose_attack(p2, self.t2.get_name())

            d1 = self.calc_damage(p1, p2, a1)
            d2 = self.calc_damage(p2, p1, a2)

            p2.take_damage(d1)
            p1.take_damage(d2)

            if p1.is_fainted() and self.t1.can_battle():
                print(f"{p1.get_name()} faitned")
                p1 = self.t1.choose_pokemon()

            if p2.is_fainted() and self.t2.can_battle():
                print(f"{p2.get_name()} fainted")
                p2 = self.t2.choose_pokemon()

        if self.t1.can_battle():
            print(f"\n{self.t1.get_name()} won")
        else:
            print(f"\n{self.t2.get_name()} won")

# pokemon types
FIRE = Type("Fire", ["Water"], ["Grass"], [])
WATER = Type("Water", ["Grass"], ["Fire"], [])
GRASS = Type("Grass", ["Fire"], ["Water"], [])
ELECTRIC = Type("Electric", ["Grass"], [], [])
PSYCHIC = Type("Psychic", [], [], [])

# charizard
BLAZE = Attack("blaze", 25, FIRE)
SOLARPOWER = Attack("solar power", 25, FIRE)

# bublabsuar
OVERGROW = Attack("overgrow", 25, GRASS)
CHLOROPHYLL = Attack("chrlorphyl", 25, GRASS)

# blastoise
TORRENT = Attack("torent", 25, WATER)
RAINDISH = Attack("rain dish", 25, WATER)

# pikachu
STATIC = Attack("static", 25, ELECTRIC)
LIGHTNINGROD = Attack("lightning rod", 25, ELECTRIC)

# psyduck
DAMP = Attack("damp", 25, PSYCHIC)
CLOUDNINE = Attack("cloud nine", 25, PSYCHIC)

# alkakazam
SYNCHRONIZE = Attack("synchronize", 25, PSYCHIC)
MAGICGUARD = Attack("magic guard", 25, PSYCHIC)

# pokemon
CHARIZARD = Pokemon("charizard", FIRE, [BLAZE, SOLARPOWER])
BULBASAUR = Pokemon("bulbasuar", GRASS, [OVERGROW, CHLOROPHYLL])
BLASTOISE = Pokemon("blastoise", WATER, [TORRENT, RAINDISH])
PIKACHU = Pokemon("pikachu", ELECTRIC, [LIGHTNINGROD, STATIC])
PSYDUCK = Pokemon("psyduck", PSYCHIC, [CLOUDNINE, DAMP])
ALAKAZAM = Pokemon("alakazam", PSYCHIC, [SYNCHRONIZE, MAGICGUARD])

# traioners
trainer1 = Trainer("trainer 1", [CHARIZARD, PSYDUCK, PIKACHU])
trainer2 = Trainer("trainer 2", [BLASTOISE, BULBASAUR, ALAKAZAM])

battle = Battle(trainer1, trainer2)
battle.start()

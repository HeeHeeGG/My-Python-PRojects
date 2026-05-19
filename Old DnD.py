import random

class Character:
    def __init__(self, name, hp, attack, armor, speed, prof):
        self.name = name
        self.base_hp = hp
        self.base_attack = attack
        self.base_armor = armor
        self.base_speed = speed
        self.base_prof = prof
        self.reset_stats()

    def reset_stats(self):
        self.hp = self.base_hp
        self.attack = self.base_attack
        self.armor = self.base_armor
        self.speed = self.base_speed
        self.prof = self.base_prof
        self.inventory = []

    def take_damage(self, damage):
        self.hp -= max(0, damage)

    def is_alive(self):
        return self.hp > 0

    def attack_opponent(self, opponent):
        attack_roll = random.randint(1, 20) + self.prof
        print(f"{self.name}'s attack is {attack_roll}.")
        
        if attack_roll >= opponent.armor:
            damage_roll = random.randint(1, self.attack)
            print(f"{self.name} hits {opponent.name} for {damage_roll} damage.")
            opponent.take_damage(damage_roll)
        else:
            print(f"{self.name}'s attack missed!")
            
        print(f"{opponent.name}'s HP: {opponent.hp}\n")
           
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}!")
        self.hp += item.hp_modifier
        self.attack += item.attack_modifier
        self.armor += item.armor_modifier
        self.speed += item.speed_modifier
        self.prof += item.prof_modifier

class Weapon:
    def __init__(self, name, damage, speed, prof, hp_modifier=0, attack_modifier=0, armor_modifier=0, speed_modifier=0, prof_modifier=0):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.prof = prof
        self.hp_modifier = hp_modifier
        self.attack_modifier = attack_modifier
        self.armor_modifier = armor_modifier
        self.speed_modifier = speed_modifier
        self.prof_modifier = prof_modifier
        
WEAPONS = [
    Weapon("Sword", random.randint(1, 10) + 3, 5, 3, hp_modifier=5, attack_modifier=3, armor_modifier=2, prof_modifier=3),
    Weapon("Axe", random.randint(1, 8) + 3, 7, 4, hp_modifier=7, attack_modifier=3, armor_modifier=1, prof_modifier=4),
    Weapon("Spear", random.randint(1, 10) + 3, 8, 4, hp_modifier=7, attack_modifier=3, armor_modifier=2, prof_modifier=4),
    Weapon("Club", random.randint(1, 12) + 4, 2, 4, hp_modifier=8, attack_modifier=2, armor_modifier=5, prof_modifier=4), 
    Weapon("Dagger", random.randint(1, 6) + 3, 11, 9, hp_modifier=2, attack_modifier=2, armor_modifier=1, prof_modifier=9)
]

def main():
    player = create_player()
    print(f"Welcome, {player.name}!")
    print("Your base stats:")
    print_stats(player)

    weapon_choice = choose_weapon()
    chosen_weapon = WEAPONS[weapon_choice - 1]
    player.add_to_inventory(chosen_weapon)
    print("Your updated stats after choosing weapon:")
    print_stats(player)

    beast = create_enemy("Beast")
    print("The Beast has arrived!")
    print_stats(beast)

    while player.is_alive() and beast.is_alive():
        print(f"{player.name}'s HP: {player.hp}")
        print(f"The Beast's HP: {beast.hp}")
        print("1. Attack")
        print("2. Run")
        choice = input("Your choice: ")
        if choice == "1":
            player.attack_opponent(beast)
            
            if beast.is_alive():
                beast.attack_opponent(player)
        elif choice == "2":
            print(f"{player.name} ran away from battle!")
            break
        else:
            print("Invalid choice. Please choose again.")


def create_player():
    name = input("Enter your name: ")
    base_hp = random.randint(95, 100)
    base_attack = random.randint(5, 12)
    base_armor = random.randint(10, 12)
    base_speed = random.randint(10, 15)
    base_prof = random.randint(3, 4)
    return Character(name, base_hp, base_attack, base_armor, base_speed, base_prof)

def create_enemy(name):
    base_hp = random.randint(100, 110)
    base_attack = random.randint(14, 20)
    base_armor = random.randint(15, 18)
    base_speed = random.randint(10, 15)
    base_prof = random.randint(3, 6)
    return Character(name, base_hp, base_attack, base_armor, base_speed, base_prof)

def choose_weapon():
    print("Pick your weapon:")
    for i, weapon in enumerate(WEAPONS):
        print(f"{i+1}. {weapon.name} - Damage: {weapon.damage}, Speed: {weapon.speed}, Proficiency: {weapon.prof}")
    while True:
        try:
            weapon_choice = int(input("Enter the number of the weapon you choose: "))
            if 1 <= weapon_choice <= len(WEAPONS):
                return weapon_choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

def declare_winner(player):
    if player.is_alive():
        print("You slayed the Enemy!")
    else:
        print("Game Over! You died.")

def print_stats(character):
    print(f"HP: {character.hp}, Attack: {character.attack}, Armor: {character.armor}, Speed: {character.speed}, Proficiency: {character.prof}")

if __name__ == "__main__":
    main()
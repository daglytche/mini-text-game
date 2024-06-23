# classes.py
import random

class Game:
    def __init__(self, player: str, player_health: int, player_damage: int, enemy_health: int, enemy_damage: int):
        self.player = player
        self.player_health = player_health
        self.player_damage = player_damage
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
   
    
    def set_enemy(self, enemy_health: int, enemy_damage: int):
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage

    def __str__(self):
        return f"Player: {self.player}, Health: {self.player_health}, Damage: {self.player_damage}"
    
    def enemy_attack(self):
        self.player_health -= self.enemy_damage
        return self.player_health #only for enemys
    
    def player_attack(self):
        self.enemy_health -= self.player_damage
        return self.enemy_health # only for players
    
    def chests(self):
        chest_luck = random.randint(0, 100)
        if chest_luck > 50:
            print("You found a nothing (add more later)!")
             # return other stuff
        elif chest_luck < 50:
            print("You found a armor!")
            return self.armor() #only for armor
        
    def door_luck(self):

        luck = random.randint(0, 100)
        if luck > 10:
            return True
        elif luck < 10:
            return False #This return false which has more options on other file, like chests
    
    def game_over(self):
        if self.player_health <= 0:
            print("GAME OVER")
            return True
        
    def armor(self):
        armortypes = ['Rusty', 'Used', 'New']
        armorpieces = ['Boots', 'Leggings', 'Chestplate', 'Helmet']
        rand_armortypes = random.choice(armortypes)
        rand_armorpieces = random.choice(armorpieces)
        armortypehealth = {'Rusty': 5, 'Used': 10, 'New': 20}
        healthbonus = armortypehealth[rand_armortypes] 
        print(f'You found a {rand_armortypes} {rand_armorpieces}, this gives you {healthbonus} hp!')
        self.player_health += healthbonus
        print(f'Your health: {self.player_health}')
        return healthbonus  
    def train(self):
        trainl = random.randint(0, 100)
        if trainl > 50:
            print("You successfully trained!")
            self.player_damage += random.randint(1, 10)
            print(f'Your damage: {self.player_damage}')
            return self.player_damage
        else:
            tfailed = print('training failed and you hurt yourself!')
            self.player_health -= random.randint(1, 10)
            print(f'Your health: {self.player_health}')
            return tfailed 
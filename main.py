from classes import * #type: ignore
import random



player = Game("samuel", 100, 10, None, None)

def enterdoor(): # this is the option to enter the door
    attackinp = None #I need a varible to do "if"
    while attackinp != "y" or attackinp != "n":
        attackinp = input("Enter the door (y/n): ")
        if attackinp.lower() == "y":
            if player.door_luck():
                print('You found a enemy!')
                enemyattackrng()
                break
            else:
                noenemyluck = random.randint(0, 100)
                if noenemyluck > 50:
                    print('You found a chest!')
                    player.chests()
                else:
                    print('Unlucky, you found nothing!')
        elif attackinp.lower() == "n":
            
            print("You chose to ignore the door")
            train = input("Do you want to train (y/n): ")
            if train.lower() == "y":
                print("You chose to train")
                player.train() # ADD A LIMIT YOU CAN TRAIN PER DOOR ENTER 
                break
            else:
                print("You chose to ignore the enemy")
                break
            
        else:
            print("Invalid input")


def enemyattackrng():
    enemyattack = random.randint(0, 100)
    if enemyattack > 50:
        print("Enemy attacked")
        player.enemy_attack()
        print(f'Your health: {player.player_health}')
        
    else:
        print("You attacked!")
        player.player_attack()
        print(f"Enemy's health: {player.enemy_health}")





enemy1 = player.set_enemy(100, 10) #makes a new enemy object

print(player) #prints the players stats

while not player.game_over(): #this is the game loop
    enterdoor()
    if player.enemy_health <= 0: # add enemy kill func to classes ltr
        print("You defeated the enemy")
        break


# RULES FOR THE PLAYER
#hit chances player rolls the dice, and if the number is 1 or 2 or 3 or 4 its a hit
#if the number is 5 or 6 its a miss
#After two hits the player wins the battle

# RULES FOR THE ENEMY
# Same rules as for the player

import random
print("you're about to fight the guard, get ready fight starts now!")
print("player goes first, lets roll a dice if you get a hit or not")


round1 = random.randint(1,100)
round2 = random.randint(1,100) # 1, 2, 3, 4, 5, 6
round3 = random.randint(1,100)

print("round 1 visar: " + str(round1))
print(f"round 2 visar: {round2}")
print("round 3 visar: " + str(round3))

result = (round1 + round2 + round3)
print("Resultaten är : ", result)
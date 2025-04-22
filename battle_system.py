import time
import random

# === Global State ===
inventory = []

# === Utility Functions ===
def slow_print(text, delay=0.035):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def add_item(item):
    if item not in inventory:
        inventory.append(item)
        slow_print(f"You picked up: {item}")

def has_item(item):
    return item in inventory

def show_inventory():
    print("\nInventory:")
    if inventory:
        for item in inventory:
            print(f" - {item}")
    else:
        print(" (empty)")

# === Game Start ===
def start_game():
    inventory.clear()
    slow_print("\nWelcome to PRISON BREAK: Shiv and Shadows\n")
    exit()
    choice = intro()
    
    if choice == "1":
        brick_path()
    elif choice == "2":
        door_path()
    else:
        slow_print("Invalid choice. Restarting...")
        start_game()

# === Game Scenes ===
def intro():
    slow_print("You wake up in a cold, dark prison cell.")
    slow_print("You have no memory of how you got here.")
    slow_print("A flickering light reveals a loose brick in the wall and a rusty door.")
    print("1. Inspect the loose brick")
    print("2. Try to open the door")
    return input("Enter 1 or 2: ")

def brick_path():
    slow_print("\nYou remove the brick and discover a narrow tunnel.")
    slow_print("Inside the hole, you find a small shiv.")
    add_item("shiv")
    print("1. Crawl through the tunnel")
    print("2. Go back and try the door")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        tunnel_escape()
    elif choice == "2":
        door_path()
    else:
        slow_print("Invalid choice. Try again.")
        brick_path()

def door_path():
    slow_print("\nThe rusty door creaks open with a loud screech.")
    slow_print("You enter a hallway and see a guard asleep at his desk.")
    slow_print("There’s a key ring on his belt.")
    print("1. Steal the keys")
    print("2. Sneak past")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        steal_keys()
    elif choice == "2":
        sneak_past()
    else:
        slow_print("Invalid choice. Try again.")
        door_path()

def steal_keys():
    slow_print("\nYou slowly approach the guard...")
    if has_item("shiv"):
        slow_print("You grip your shiv tightly, just in case.")
        print("1. Threaten the guard")
        print("2. Steal the keys silently")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            slow_print("You jab the shiv close to his neck. His eyes snap open.")
            slow_print("\"Don't move,\" you whisper. He freezes in fear.")
            slow_print("You grab the key ring from his belt and back away.")
            add_item("prison key")
            escape_with_key(threatened=True)
        elif choice == "2":
            silent_key_steal()
        else:
            slow_print("Invalid choice. Try again.")
            steal_keys()
    else:
        silent_key_steal()

def silent_key_steal():
    slow_print("You carefully reach for the keys...")
    time.sleep(2)
    slow_print("The guard stirs...")
    success = random.choice([True, False])
    if success:
        slow_print("...but stays asleep. You get the keys!")
        add_item("prison key")
        escape_with_key(threatened=False)
    else:
        slow_print("...and wakes up! He's coming at you!")
        fight_guard()

def fight_guard():
    player_hp = 20
    guard_hp = 15
    defending = False

    slow_print("\nA guard wakes up and attacks!")

    while player_hp > 0 and guard_hp > 0:
        print(f"\nYour HP: {player_hp} | Guard HP: {guard_hp}")
        print("1. Attack")
        print("2. Defend")
        print("3. Try to Run")
        choice = input("→ ")

        if choice == "1":
            base_damage = random.randint(4, 7)
            if has_item("shiv"):
                base_damage += random.randint(3, 5)
                slow_print("You slash with your shiv!")
            else:
                slow_print("You punch the guard!")
            guard_hp -= base_damage
            slow_print(f"You deal {base_damage} damage.")
        elif choice == "2":
            defending = True
            slow_print("You brace for the guard’s attack.")
        elif choice == "3":
            if random.random() < 0.5:
                slow_print("You slip away while the guard stumbles!")
                return
            else:
                slow_print("You try to run but he grabs you!")
        else:
            slow_print("Invalid action.")

        if guard_hp > 0:
            guard_attack = random.randint(3, 6)
            if defending:
                guard_attack = max(1, guard_attack - random.randint(2, 4))
                slow_print("You absorb some of the damage.")
                defending = False
            player_hp -= guard_attack
            slow_print(f"The guard hits you for {guard_attack} damage.")

    if player_hp <= 0:
        slow_print("\nYou collapse. The guard calls for backup.")
        show_inventory()
        slow_print("GAME OVER – You died in combat.")
        end_game()
    else:
        slow_print("\nYou knock the guard out cold!")
        add_item("prison key")
        escape_with_key(threatened=False)

def tunnel_escape():
    slow_print("\nYou squeeze through the tunnel. It's dark and damp.")
    slow_print("Halfway through, you hear whispering...")
    slow_print("Another prisoner is trapped in a side cell you pass.")
    slow_print("He begs: \"Please... help me get out too!\"")
    print("1. Help the prisoner")
    print("2. Keep going")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        if has_item("shiv"):
            slow_print("You use the shiv to pry open the cell bars. He crawls into the tunnel with you.")
            add_item("rescued prisoner")
            heroic_escape()
        else:
            slow_print("You try to help, but without a tool, you can't break the lock.")
            slow_print("You apologize and move on...")
            silent_escape()
    elif choice == "2":
        silent_escape()
    else:
        slow_print("Invalid choice. Try again.")
        tunnel_escape()

def sneak_past():
    slow_print("\nYou tiptoe past the guard...")
    time.sleep(2)
    slow_print("CRASH! You bump into a mop bucket.")
    slow_print("The guard wakes up and sounds the alarm.")
    slow_print("You're surrounded. The escape attempt has failed.")
    show_inventory()
    slow_print("GAME OVER – Caught while sneaking.")
    end_game()

def escape_with_key(threatened=False):
    slow_print("You sneak down the hall to the main gate.")
    slow_print("You use the prison key to unlock the heavy door.")
    slow_print("The cool night air hits your face.")
    if threatened:
        bloody_escape()
    else:
        silent_escape()

# === Endings ===
def heroic_escape():
    slow_print("You and the rescued prisoner crawl out behind the prison yard.")
    slow_print("You share a look – survivors.")
    show_inventory()
    slow_print("HEROIC ENDING: You escaped and saved someone else.")
    end_game()

def silent_escape():
    slow_print("You emerge quietly outside, behind the prison yard.")
    show_inventory()
    slow_print("SILENT ENDING: You escaped without a trace.")
    end_game()

def bloody_escape():
    show_inventory()
    slow_print("BLOODY ENDING: You escaped by threatening or fighting a guard.")
    end_game()

def end_game():
    print("\nWould you like to play again? (y/n)")
    choice = input("→ ").lower()
    if choice == 'y':
        start_game()
    else:
        slow_print("Thanks for playing. Stay sharp.")

# === Start the game ===
start_game()
    
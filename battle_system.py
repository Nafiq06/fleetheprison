import time
import random

# Inventory system
inventory = []

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def add_item(item):
    if item not in inventory:
        inventory.append(item)
        slow_print(f"🧳 You picked up: {item}")

def has_item(item):
    return item in inventory

def show_inventory():
    slow_print("\n📦 Inventory:")
    if inventory:
        for item in inventory:
            slow_print(f" - {item}")
    else:
        slow_print("Your inventory is empty.")

# === Game Scenes ===

def intro():
    slow_print("You wake up in a cold, dark prison cell.")
    slow_print("You have no memory of how you got here.")
    slow_print("A flickering light reveals a loose brick in the wall and a rusty door.")
    slow_print("What do you want to do?")
    slow_print("1. Inspect the loose brick")
    slow_print("2. Try to open the door")
    return input("Enter 1 or 2: ")

def brick_path():
    slow_print("\nYou remove the brick and discover a narrow tunnel.")
    slow_print("Inside the hole, you find a small shiv.")
    add_item("shiv")
    slow_print("Do you want to crawl through the tunnel?")
    slow_print("1. Yes, crawl through the tunnel")
    slow_print("2. No, go back and try the door")
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
    slow_print("Do you try to steal the keys or sneak past him?")
    slow_print("1. Steal the keys")
    slow_print("2. Sneak past")
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
        slow_print("Do you want to use the shiv to threaten the guard or try to steal the keys quietly?")
        slow_print("1. Threaten the guard")
        slow_print("2. Steal the keys silently")
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
        slow_print("...and wakes up! He yells for help.")
        slow_print("You’re tackled by two more guards within seconds.")
        show_inventory()
        slow_print("🚨 GAME OVER – You were caught.")
        end_game()

def tunnel_escape():
    slow_print("\nYou squeeze through the tunnel. It's dark and damp.")
    slow_print("Halfway through, you hear whispering...")
    slow_print("Another prisoner is trapped in a side cell you pass.")
    slow_print("He begs: \"Please... help me get out too!\"")
    slow_print("Do you help him?")
    slow_print("1. Yes, help the prisoner")
    slow_print("2. No, keep going")
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
    slow_print("🌟 HEROIC ENDING: You escaped and saved someone else. Not all heroes wear capes.")
    end_game()

def silent_escape():
    slow_print("You emerge quietly outside, behind the prison yard. No alarms. No violence.")
    show_inventory()
    slow_print("🌙 SILENT ENDING: You escaped without a trace. A ghost in the night.")
    end_game()

def bloody_escape():
    show_inventory()
    slow_print("🩸 BLOODY ENDING: You escaped by threatening a guard. You're free… but at what cost?")
    end_game()

def sneak_past():
    slow_print("\nYou tiptoe past the guard...")
    time.sleep(2)
    slow_print("CRASH! You bump into a mop bucket.")
    slow_print("The guard wakes up and sounds the alarm.")
    slow_print("You're surrounded. The escape attempt has failed.")
    show_inventory()
    slow_print("🚨 GAME OVER – Caught while sneaking.")
    end_game()

def end_game():
    slow_print("\nWould you like to play again? (y/n)")
    choice = input("→ ").lower()
    if choice == 'y':
        inventory.clear()
        start_game()
    else:
        slow_print("Thanks for playing! Stay sneaky.")

# === Start Game ===

def start_game():
    choice = intro()
    if choice == "1":
        brick_path()
    elif choice == "2":
        door_path()
    else:
        slow_print("Invalid choice. Restart the game and choose 1 or 2.")
        start_game()

# Launch game
start_game()

 
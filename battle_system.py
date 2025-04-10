def start_game():
    print("\nWelcome to the prison!")
    print("You are in a prison you need to escape from there!. You have free time outside of the cell, you decide to explore the prison to plan your escape.")
    
    while True:
        print("\nWhat would you like to do, you are in a prison cell?")
        print("1. Explore the prison.")
        print("2. Quit the game.")
        
        
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            explore_prison()
        
        
        elif choice == "2":
            print("\nThanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def explore_prison():
    print("\nYou decide to explore the prison. And see some guards.")
    
    while True:
        print("\nYou have two paths to choose from:")
        print("1. Take the path to the left to cafereria.")
        print("2. Take the path to the right.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            left_path()
        elif choice == "2":
            right_path()
        else:
            print("Invalid choice. Please try again.")

def left_path():
    print("\nYou walk down to the left path and found the cafeteria with crowded people.")
    
    while True:
        print("\nWhat do you want to do?")
        print("1. hide amoungst your inmates.")
        print("2. Return back and go down the right path.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            print("\nYou found an exit from ventilation, and escaped from there")
            game_won()
        elif choice == "2":
            explore_prison()  # Return to the main prison exploration
        else:
            print("Invalid choice. Please try again.")

def right_path():
    print("\nYou walk down the right path and encounter a guard!")
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Fight the guard.")
        print("2. Run away.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            ### ADD FIGHTING SYSTEM HERE! ###
            
            
            print("\nYou fought the guard, and got his keycard.")
            game_won()
        elif choice == "2":
            print("\nYou decide to hide from the guards from seeing you!!!")
            wait_for_others()
             # Go back to explore the prison again

        else:
            print("Invalid choice. Please try again.")

def wait_for_others():
    print("your hiding in a corner")
    exit()
    while True:
        print("\nWhat would you like to do next?")
        print("1. Go back and explore the prison.")
        print("2. Quit the game.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            start_game()  # Go back to start the game again
        elif choice == "2":
            print("\nThanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def game_over():
    print("\nGame Over! You alerted the guards!!!")
    
    while True:
        print("\n1. Yes, try again.")
        print("2. No, quit the game.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            start_game()
        elif choice == "2":
            print("\nThanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def game_won():
    print("\nCongratulations! You've escaped the jail!")
    print("wanna play again?")
    
    while True:
        print("\n1. Play again.")
        print("2. Quit the game.")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            start_game()
        elif choice == "2":
            print("\nThanks for playing! Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Start the game
start_game()
 
import random
import art
import game_data
#import replit

def clear():
    """Clears the console"""
    print("\n"*47)

def selection():
    """selects a random entry from the game data file"""
    selection = random.choice(game_data.data)
    return selection

def print_data(selection):
    """Extracts the data from dictionary and prints out its values"""
    name = selection["name"]
    description = selection["description"]
    country = selection["country"]
    return f"{name}, a {description}, from {country}."

def follower_comparison(a, b):
    """Determines whether a or b has more followers"""
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"

def game():
    a = selection()
    b = selection()
    score = 0
    should_continue = True
    print(art.logo)
    
    while should_continue == True:
        a = b
        b = selection()
        while a == b:
            b = selection()
            
        print(f"Compare A: " + print_data(a))
        print(art.vs)
        print(f"Against B: " + print_data(b))
        
        winner = follower_comparison(a, b)
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()
        #replit.clear()
        print(art.logo)

        if choice == winner:
            score += 1         
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorrt, that's wrong. Your final score is {score}.")
            should_continue = False

game()

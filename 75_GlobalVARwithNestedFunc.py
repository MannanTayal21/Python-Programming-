# Question: write a python code to demonstrate global variables with nested function.

# 1. This is our GLOBAL score variable, available everywhere in the program.
main_game_score = 100

def outer_manager():
    # The outer function's job is to run the update.
    print(f"Outer function sees the starting score: {main_game_score}")

    def inner_updater():
        # The nested function is where the action happens!
        
        # We MUST use the 'global' keyword to tell Python:
        # "I want to change the score that's defined at the very top, not a new one!"
        global main_game_score
        
        # Now we update the GLOBAL variable
        main_game_score = 500
        print(f"--- Nested function updated the score to: {main_game_score} ---")

    # Run the nested function to make the change
    inner_updater()
    
    # The outer function sees the new, changed global score
    print(f"Outer function now sees the final score: {main_game_score}")

# Check the global score before we call any functions
print(f"Before running the manager: The global score is: {main_game_score}")

# Run the entire process
outer_manager()

# Check the global score one last time to confirm the nested function's change stuck
print(f"After running the manager: The final global score is: {main_game_score}")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)

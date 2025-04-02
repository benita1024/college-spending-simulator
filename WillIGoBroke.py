import random  # Importing the random module to simulate probabilistic transitions

# Define the Markov transition model:
# Each state maps to a dictionary of actions, which map to lists of (next_state, probability) pairs
transitions = {
    "Stable": {
        "Cook at Home": [("Stable", 0.75), ("Struggling", 0.20), ("Broke", 0.05)],
        "Buy Merch": [("Stable", 0.40), ("Struggling", 0.45), ("Broke", 0.15)],
        "Eat Out": [("Stable", 0.50), ("Struggling", 0.35), ("Broke", 0.15)],
        "Skip Spending": [("Stable", 0.80), ("Struggling", 0.15), ("Broke", 0.05)],
        "Free Campus Event": [("Stable", 0.70), ("Struggling", 0.25), ("Broke", 0.05)]
    },
    "Struggling": {
        "Cook at Home": [("Stable", 0.30), ("Struggling", 0.60), ("Broke", 0.10)],
        "Buy Merch": [("Stable", 0.05), ("Struggling", 0.45), ("Broke", 0.50)],
        "Eat Out": [("Stable", 0.10), ("Struggling", 0.55), ("Broke", 0.35)],
        "Skip Spending": [("Stable", 0.35), ("Struggling", 0.55), ("Broke", 0.10)],
        "Free Campus Event": [("Stable", 0.25), ("Struggling", 0.60), ("Broke", 0.15)]
    },
    "Broke": {
        "Cook at Home": [("Struggling", 0.20), ("Broke", 0.70), ("Bankrupt", 0.10)],
        "Buy Merch": [("Broke", 0.30), ("Bankrupt", 0.70)],
        "Eat Out": [("Broke", 0.50), ("Bankrupt", 0.45), ("Struggling", 0.05)],
        "Skip Spending": [("Struggling", 0.25), ("Broke", 0.65), ("Bankrupt", 0.10)],
        "Free Campus Event": [("Struggling", 0.15), ("Broke", 0.70), ("Bankrupt", 0.15)]
    },
    "Bankrupt": {
        "Any": [("Bankrupt", 1.0)]  # Absorbing state: once Bankrupt, you stay there
    }
}

# List of available actions for the player to choose from each day
actions = ["Cook at Home", "Buy Merch", "Eat Out", "Skip Spending", "Free Campus Event"]

# Function to determine the next financial state based on current state and chosen action
def choose_next_state(current_state, action):
    # Get the list of possible next states and probabilities for the given state and action
    options = transitions[current_state][action] if current_state != "Bankrupt" else transitions["Bankrupt"]["Any"]
    r = random.random()  # Generate a random float between 0 and 1
    cumulative = 0  # Initialize cumulative probability
    for next_state, prob in options:  # Loop through possible transitions
        cumulative += prob  # Accumulate probabilities
        if r <= cumulative:  # If random number falls in the current interval, return this state
            return next_state
    return options[-1][0]  # Fallback: return the last state's name (shouldn't happen if probabilities sum to 1)

# Function to run the 7-day financial simulation
def run_simulation(days=7):
    state = "Stable"  # Start the simulation in the "Stable" state
    print("Starting your week with financial status:", state)

    # Loop through each day of the simulation
    for day in range(1, days + 1):
        if state == "Bankrupt":  # If user is bankrupt, end simulation early
            print(f"Day {day}: You're bankrupt. Game over 💀")
            break

        # Display current day and status
        print(f"\nDay {day} — Your current status: {state}")
        print("Choose your action:")
        
        # Print numbered list of actions for the user to choose from
        for i, act in enumerate(actions, 1):
            print(f"{i}. {act}")

        # Get valid user input
        while True:
            try:
                choice = int(input("Enter the number of your action: "))  # User selects an action by number
                if 1 <= choice <= len(actions):  # Ensure choice is within valid range
                    action = actions[choice - 1]  # Map number to action name
                    break
            except ValueError:  # Handle non-integer inputs
                pass
            print("Invalid input. Try again.")  # Prompt again on invalid input

        # Determine the next state based on current state and action
        new_state = choose_next_state(state, action)
        print(f"You chose: {action} → Now you're: {new_state}")  # Show result of action
        state = new_state  # Update current state

    # After the loop ends, print final financial state
    print("\nWeek over! Your final financial state is:", state)

# Call the simulation function to start the game
run_simulation()

"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Starting room
current_room = "Great Hall"

# Game loop
while True:
    # Display current room
    print("\nYou are in the", current_room)

# Ask player for a direction
direction = input(
    "Enter a direction (north, south, east, west)
    "or 'exit' to quit: "
) .strip() .lower()

# Exit the game
if direction == "exit":
    print("Thanks for playing!")
    break

# Check for valid movement 
elif direction in rooms[current_room]:
    current_room = room [current_room][direction]
    print("You moved to the", current_room)

#Invalid movement 
else:
    print("Invalid direction. Try again.")




# TODO: Run and debug all milestone cases in prototype/README.md.

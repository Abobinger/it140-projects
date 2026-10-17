"""Project Two starter for the student's text-based adventure game."""
#Alesa Bobinger


def show_instructions():
    """Display the story, goal, and available commands."""
    print("Murder Mystery Party")
    print("One of your party guests is a murderer!")
    print("Search the house and collect all 6 items before entering the Bedroom.")
    print("Entering the Bedroom without all 6 items means you lose.")
    print("Move: go north, go south, go east, go west")
    print("Collect: get <item name> (use the name displayed in the room)")
    print("The Kitchen and Dining Room each contain a separate bloody steak knife.")


def show_status(current_room, inventory, rooms):
    """Show the player's location, inventory, nearby item, and exits."""
    print("\n" + "-" * 40)
    print("You are in the", current_room)
    print("Inventory:", inventory)
    print("Items collected:", len(inventory), "of 6")
    item = rooms[current_room].get("item")
    if item:
        print("You see:", item)
    print("Available directions:", ", ".join(
        direction for direction in rooms[current_room] if direction != "item"
    ))


def main():
    """Run the game using the rooms and items from the project map."""
    rooms = {
        "Entrance Way": {
            "north": "Kitchen", "south": "Dining Room",
            "east": "Library", "west": "Office"
        },
        "Kitchen": {
            "south": "Entrance Way", "east": "Wine Cellar",
            "item": "Bloody Steak Knife"
        },
        "Wine Cellar": {"west": "Kitchen", "item": "A Gun"},
        "Office": {"east": "Entrance Way", "item": "Torn Fabric"},
        "Dining Room": {
            "north": "Entrance Way", "east": "Bar",
            "item": "Bloody Steak Knife"
        },
        "Bar": {"west": "Dining Room", "item": "Whiskey"},
        "Library": {
            "west": "Entrance Way", "north": "Bedroom",
            "item": "A Note from a Guest"
        },
        "Bedroom": {"south": "Library"}
    }
    current_room = "Entrance Way"
    inventory = []
    required_items = 6
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        # Check the ending before accepting another command in the villain room.
        if current_room == "Bedroom":
            if len(inventory) == required_items:
                print("You collected all 6 items and exposed the murderer!")
                print("Congratulations! You solved the mystery. YOU WIN!")
            else:
                print("The murderer catches you before you gather all the evidence!")
                print("GAME OVER!")
            break

        # Normalize spaces and capitalization while preserving multiword items.
        command = " ".join(input("Enter your command: ").strip().split())
        parts = command.split(" ", 1)
        action = parts[0].lower()
        target = parts[1].lower() if len(parts) == 2 else ""

        if action == "go":
            if target not in ("north", "south", "east", "west"):
                print("Use go north, go south, go east, or go west.")
            elif target in rooms[current_room]:
                current_room = rooms[current_room][target]
            else:
                print("You cannot go that way.")
        elif action == "get":
            item = rooms[current_room].get("item")
            if not target:
                print("Enter get followed by the item name.")
            elif item is None:
                print("There is no item to collect in this room.")
            elif target == item.lower():
                inventory.append(item)
                # Removing the room's item prevents collecting it twice.
                del rooms[current_room]["item"]
                print("You collected:", item)
            else:
                print("That item is not here. Use the item name shown above.")
        else:
            print("Invalid command. Use go <direction> or get <item name>.")

    print("Thanks for playing Murder Mystery Party!")








if __name__ == "__main__":
    main()

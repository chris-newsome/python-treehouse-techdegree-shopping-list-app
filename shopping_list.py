import os

# Creates new empty list
shopping_list = []

def clear_screen():
    """Function that uses the OS module to clear the screen when the user wants to play again"""

    os.system("cls" if os.name == "nt" else "clear")

def add_to_list(item):
    """Function that adds items to the list"""

    show_list()

    if len(shopping_list):

        position = input("Where should I add {}?\n"
            "Press ENTER to add to the end of the list\n"
                "> ".format(item))
                
    else:

        position = 0
    
    try:

        position = abs(int(position))
    
    except ValueError:

        position = None
    
    if position is not None:

        shopping_list.insert(position-1, item)

    else:

        shopping_list.append(new_item)

    show_list()

def show_list():
    """Function to show user the list in its current state"""

    clear_screen()

    print("Here's your list:")

    # Variable for finding the position of a list item
    index = 1

    for item in shopping_list:

        print("{}. {}".format(index, item))

        index += 1

    print("-"*10)

def show_help():
    """Function to prompt the user about items in the cart"""

    clear_screen()

    print("What should we pick up at the store?")

    print("""

    Enter 'DONE' to stop adding items.

    Enter 'HELP' for this help.

    Enter 'SHOW' to see your current list.

    """)

show_help()

# User is continually prompted to add item
while True:

    new_item = input("> ")

    # When user is done, exit the loop
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':

        break

    elif new_item.upper() == 'HELP':

        show_help()

        continue

    elif new_item.upper() == 'SHOW':

        show_list()

        continue

    else:
        
        add_to_list(new_item)
    
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)

show_list()
    
# Creates new empty list
shopping_list = []

# Function that adds items to the list
def add_to_list(item):
    shopping_list.append(item)

    # Notify the user that the item was added and state the number of items in the list
    print("Added! The list has {} items".format(len(shopping_list)))

# Function to show user the list in its current state
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

# Function to prompt the user about items in the cart
def show_help():
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
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)

show_list()
    
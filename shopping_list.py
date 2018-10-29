import os

# This is our Shopping List app
# This will ask us what we what to buy to be added to our shopping list

# Constants
SHOPPING_LIST = []


# Functions
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help. 
Enter 'SHOW' to be shown the total list at any time. 
Enter 'REMOVE' to delete an item from your list.
""")


def add_to_list(item):
    show_list(SHOPPING_LIST)
    if len(SHOPPING_LIST):
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
        SHOPPING_LIST.insert(position - 1, item)  
    else:
        SHOPPING_LIST.append(item)                     
    show_list(SHOPPING_LIST)    
    return SHOPPING_LIST


def remove_from_list():
    show_list(SHOPPING_LIST)
    what_to_remove = input("What item do you want to remove?\n> ")
    try:    
        if what_to_remove != SHOPPING_LIST:
            raise ValueError("{} is not in the shopping list".format(what_to_remove))
        else:
            SHOPPING_LIST.remove(what_to_remove)      
    except ValueError as err:
        print("Not right")
        print("({})".format(err))
    show_list(SHOPPING_LIST)


def show_list(items):
    clear_screen()
    print("Here's your list:")
    index = 1
    for item in items:
        print("{}. {}".format(index, item))
        index += 1
    print("-" * 10)

# Call show_help function at the beginning of the app
show_help()
# Set up a loop
while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT": 
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list(SHOPPING_LIST)
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        continue
    else:
        # call function to add new_item to the shopping_list
        add_to_list(new_item)

# Show our total list at the end
show_list(SHOPPING_LIST)
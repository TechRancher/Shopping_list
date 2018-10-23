# This is our Shopping List app
# This will ask us what we what to buy to be added to our shopping list

# Constants
SHOPPING_LIST = []



# Functions
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help. 
Enter 'SHOW' to be shown the total list at any time. 
""")


def add_to_list(item):
    SHOPPING_LIST.append(item)
    # Notify user how many items are in the shopping list
    print("Item added! There are {} items in the list." .format(len(SHOPPING_LIST)))
    return SHOPPING_LIST


def show_list(items):
    print("Here's your list:")
    for item in items:
        print(item)


# Call show_help function at the begining of the app
show_help()
# Set up a loop
while True:
    new_item = input("> ")
    
    if new_item == "DONE": 
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list(SHOPPING_LIST)
        continue

    # call function to add new_item to the shopping_list
    add_to_list(new_item)

show_list(SHOPPING_LIST)
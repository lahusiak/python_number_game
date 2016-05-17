# This is a shopping list application
# Created with Treehouse Python Basics course


# make a list to hold onto our items
shopping_list = []

def show_help():
    #show instructions
    print("What do you need to do today?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

show_help()

def show_list():
    # print out the list
    print("Here's the list")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to out list
        shopping_list.append(new_item)
        print("Added {}. list now has {} items.".format(new_item, len(shopping_list)))
while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == "DONE":
            break
        elif new_item == "SHOW":
            show_list()
            continue
        elif new_item == "HELP":
            show_help()
            continue
        add_to_list(new_item)

show_list()

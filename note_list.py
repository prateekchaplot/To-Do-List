import os


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


def help():
    print("* Enter Q exit *")
    print("* Enter S to show list *")
    print("* Enter R to remove item from list *")


def show():
    clear_screen()

    print("Note List:")
    print("-"*10)

    for index in range(len(user_list)):
        print("{}. {}".format(index+1, user_list[index]))


def remove():
    show()
    print("\n* Enter index of the item to remove that item *")
    print("* Press ENTER if you don't want to delete any item *\n")
    
    try:
        index = int(input("> ")) - 1
    except ValueError:
        print("List Unchanged!")
    else:
        if index in range(len(user_list)):
            print("Removed:", user_list[index])
            del user_list[index]
        else:
            print("* Invalid index selected... *")
    

clear_screen()
print("\n ** Welcome to Note List **", end="")
input()
user_list = []

while True:
    clear_screen()
    help()
    
    item = input("> ")
    
    if item.lower() == 'q':
        break
    elif item.lower() == 's':
        show()
        input("Press return to continue...")
        continue
    elif item.lower() == 'r':
        remove()
        input("Press return to continue...")
        continue

    user_list.append(item)

show()